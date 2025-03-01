import React from 'react';
import { Link } from 'react-router-dom';
;


export default function Home() {
    return (
        <div style={{ backgroundColor: '#001f3f', color: '#FFD700', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
            {/* Header */}
            <header style={headerStyle}>
                <img
                    src="logo.jpg"
                    alt="Лого на Македонска берза"
                    style={{ height: '60px', marginRight: '20px' }}
                />
                <nav style={navStyle}>
                    <Link to="/" style={linkStyle}>Home</Link>
                    <Link to="/show-data" style={linkStyle}>Show Data</Link>
                    <Link to="/about" style={linkStyle}>About</Link>
                    <Link to="/technical-analysis">Погледни техничка анализа</Link>
                </nav>
            </header>

            {/* Main Content */}
            <main style={mainContentStyle}>
                <h1 style={{ fontSize: '3em', textShadow: '2px 2px 5px rgba(0, 0, 0, 0.7)' }}>Македонска берза</h1>
                <p style={{ fontSize: '1.2em', fontStyle: 'italic' }}>Информации за акциите од последната деценија</p>
            </main>

            {/* Footer */}
            <footer style={footerStyle}>
                <p>© 2024 Македонска берза. Сите права се задржани.</p>
            </footer>
        </div>
    );
}

//css
const headerStyle = {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: '#001f3f',
    padding: '10px 20px',
    borderBottom: '2px solid #FFD700',
    color: '#FFD700',
};

const navStyle = {
    display: 'flex',
    gap: '15px',
};

const linkStyle = {
    color: '#FFD700',
    textDecoration: 'none',
    fontSize: '1.1em',
    fontWeight: 'bold',
    transition: 'color 0.3s',
};

linkStyle[':hover'] = {
    color: '#FFA500',
};

const mainContentStyle = {
    flex: 1,
    textAlign: 'center',
    padding: '50px 20px',
};

const footerStyle = {
    textAlign: 'center',
    padding: '15px 0',
    backgroundColor: '#001f3f',
    color: '#FFD700',
    borderTop: '2px solid #FFD700',
};



