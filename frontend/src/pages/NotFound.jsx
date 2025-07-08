function NotFound() {
    return (
        <div style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            minHeight: '80vh',
            backgroundColor: '#ffffff',
            padding: '2rem'
        }}>
            <div style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                backgroundColor: '#f8f9fa',
                borderRadius: '12px',
                padding: '3rem',
                textAlign: 'center',
                boxShadow: '0 4px 20px rgba(0, 0, 0, 0.1)',
                maxWidth: '500px',
                width: '100%'
            }}>
                <h1 style={{
                    fontSize: '6rem',
                    margin: '0',
                    color: '#495057',
                    fontWeight: 'bold'
                }}>
                    404
                </h1>
                <h2 style={{
                    fontSize: '2rem',
                    margin: '1rem 0',
                    color: '#343a40'
                }}>
                    Page Not Found
                </h2>
                <p style={{
                    fontSize: '1.1rem',
                    color: '#6c757d',
                    marginBottom: '2rem',
                    lineHeight: '1.6'
                }}>
                    Sorry, the page you're looking for doesn't exist.
                </p>
                <a
                    href="/"
                    style={{
                        padding: '12px 24px',
                        backgroundColor: '#007bff',
                        color: 'white',
                        textDecoration: 'none',
                        borderRadius: '6px',
                        fontSize: '1rem',
                        transition: 'background-color 0.3s ease',
                        border: 'none',
                        cursor: 'pointer'
                    }}
                    onMouseOver={(e) => e.target.style.backgroundColor = '#0056b3'}
                    onMouseOut={(e) => e.target.style.backgroundColor = '#007bff'}
                >
                    Go Back Home
                </a>
            </div>
        </div>
    );
}

export default NotFound;