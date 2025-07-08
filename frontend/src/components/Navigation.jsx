import { Link } from 'react-router-dom';

function Navigation() {
    return (
        <nav style={{ padding: '1rem', borderBottom: '1px solid #ccc' }}>
            <Link to="/" style={{ margin: '0 1rem', textDecoration: 'none' }}>
                Home
            </Link>
        </nav>
    );
}

export default Navigation;