"""
Weather Station simulation
"""

import threading
import time
import random
import socket
import json

STATIONS = [
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

MAX_N_TRIES = 5  # Maximum number of connection attempts
TIME_BETWEEN_TRIES = 5
SAMPLING_TIME = 5

class WeatherStation:
    #id
    #name
    #token
    def __init__(self, station_id, name, token):
        self.station_id = station_id
        self.name = name
        self.token = token

    def simulation(self):
        """
        Simulate a weather station
        """

        def connect_to_server():
            print(f"[{self.name}] connecting with token: {self.token}")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            n_tries = 0
            while n_tries < MAX_N_TRIES:
                try:
                    sock.connect(('localhost', 9000))
                    print(f"Station {self.station_id} connected to server.")
                    return sock
                except socket.error as e:
                    if n_tries >= MAX_N_TRIES - 1:
                        return None
                    else:
                        print(f"Station {self.station_id} failed to connect: {e}, retrying in {TIME_BETWEEN_TRIES} seconds)")
                        n_tries += 1
                        time.sleep(TIME_BETWEEN_TRIES)
        

        def authenticate():
            #send the authentication token to the server
            try:
                sock.send(self.token.encode('utf-8'))
            except Exception as e:
                print(e)
                print(f"\n\n\nclosing thread {threading.current_thread().name}")
            
            data = sock.recv(1024)
            auth_response = data.decode('utf-8').strip()
            print("auth_response:", auth_response)
            if auth_response.lower() == "invalid token":
                sock.close()
                return False
            return True
        
        time.sleep(5) # wait for the server to start, TODO: will change this in the future implementing health checks to the container

        sock = connect_to_server()
        if not sock:
            print(f"Station {self.station_id} could not connect to server after {MAX_N_TRIES} attempts, exiting...")
            return
        auth = authenticate()
        if not auth:
            print(f"Invalid token ({self.token}), exiting...")
            return

        while True:
            metrics_to_send = {}
            for sensor in STATIONS[self.station_id]["sensors"]:
                if sensor == "temperature":
                    metrics_to_send["temperature"] = random.uniform(-10, 40)
                elif sensor == "humidity":
                    metrics_to_send["humidity"] = random.uniform(0, 100)
            print("\n\n")
            print(metrics_to_send)
            print("\n\n")
            json_metrics = json.dumps(metrics_to_send).encode('utf-8')
            sock.send(str(len(json_metrics)).encode('utf-8'))
            sock.send(json_metrics)
            time.sleep(SAMPLING_TIME)


if __name__ == "__main__":    
    # Create and start a thread for each weather station
    threads = []
    for station in STATIONS:
        ws = WeatherStation(station["id"], station["name"], station["token"])
        thread = threading.Thread(target=ws.simulation)
        thread.daemon = True  # Thread will die when main program exits
        thread.start()
        threads.append(thread)
    
    # Keep the main thread alive to allow the simulation to run
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopping weather station simulations...")