import socket
import threading
import json

AUTH_TOKEN_LEN = 16  # Length of the authentication token

STATIONS = [ #TODO fetch these from the db
    {
        "id": 0,
        "name": "Senigallia",

        "latitude": 43.714952,
        "longitude": 13.217949,
        
        "token": "secret_tokennnnn",
        "sensors": ["temperature", "humidity"],
    },
    {
        "id": 1,
        "name": "Jesi",

        "latitude": 43.522783,
        "longitude": 13.243787,

        "token": "0123456789ciaooo",
        "sensors": ["temperature"],
    },
    {
        "id": 2,
        "name": "Bologna",

        "latitude": 44.49382,
        "longitude": 11.342633,

        "token": "tokennnnn_secret",
        "sensors": ["temperature", "humidity"],
    },
]



def handle_client(client_socket, client_address):
    """Handle communication with a connected client"""
    print(f"[{threading.current_thread().name}] New connection from {client_address}")
    
    try:
        # AUTHENTICATION
        data = client_socket.recv(AUTH_TOKEN_LEN)
            
        auth_token = data.decode('utf-8').strip()
        print(f"[{threading.current_thread().name}] Received: {auth_token}")

        connecting_station = next((station for station in STATIONS if station["token"] == auth_token), None)
        if not connecting_station:
            print("Invalid token (not found in STATIONS)")
            response = "Invalid token"
            client_socket.send(response.encode('utf-8'))
            client_socket.close()
            return
        else:
            print("Valid token")
            response = "Token accepted"
            client_socket.send(response.encode('utf-8'))
        
        threading.current_thread().name = connecting_station['name']
        print(f"[{threading.current_thread().name}] Connection established with {client_address}")
        
        # DATA RECEIVING LOOP
        while True:
            # Receive data from client
            msg_len = int(client_socket.recv(4).decode('utf-8').strip())
            metrics = client_socket.recv(msg_len).decode('utf-8').strip()

            json_metrics = json.loads(metrics)
            print(f"Metric saved: {json_metrics}...") #TODO save this to the db

    except ConnectionResetError:
        print(f"[{threading.current_thread().name}] Client {client_address} disconnected unexpectedly")
    except Exception as e:
        print(f"[{threading.current_thread().name}] Error handling client {client_address}: {e}")
    finally:
        client_socket.close()
        print(f"[{threading.current_thread().name}] Connection with {client_address} closed")


class IoTSERVER:
    """
    ATTRIBUTES:
    #host
    #port
    #socket
    #running flag
    """
    
    def __init__(self, host='localhost', port=9000):
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
    
    def start(self):
        """Start the TCP server"""
        try:
            # Create socket
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Bind and listen
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            self.running = True
            
            print(f"IoT Server listening on {self.host}:{self.port}")
            print("Press Ctrl+C to stop the server")
            
            while self.running:
                try:
                    # Accept new connection
                    client_socket, client_address = self.server_socket.accept()
                    
                    # Create and start new thread for this client
                    client_thread = threading.Thread(
                        target=handle_client,
                        args=(client_socket, client_address),
                        name=f"Client-{client_address[0]}:{client_address[1]}"
                    )
                    client_thread.daemon = True  # Thread will die when main program exits
                    client_thread.start()
                    
                except socket.error as e:
                    if self.running:  # Only print error if server is supposed to be running
                        print(f"Socket error: {e}")
                        
        except KeyboardInterrupt:
            print("\nShutting down server...")
        except Exception as e:
            print(f"Server error: {e}")
        finally:
            self.stop()
    
    def stop(self):
        """Stop the server"""
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        print("Server stopped")

def main():
    # Create and start server
    server = IoTSERVER('localhost', 9000)
    server.start()

if __name__ == "__main__":
    main()