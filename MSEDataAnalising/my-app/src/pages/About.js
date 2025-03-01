import React from 'react';
import { Link } from 'react-router-dom';

export default function About() {
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
                </nav>
            </header>


            <main style={mainContentStyle}>
                <h1 style={{ fontSize: '3em', textShadow: '2px 2px 5px rgba(0, 0, 0, 0.7)' }}>За Македонска Берза</h1>
                <p style={{ fontSize: '1.2em', fontStyle: 'italic' }}>
                    Главната мисија на Берзата е да ни овозможи безбедно, корисно и транспарентно тргување
                    со акции во Република Македонија.

                    Во оваа апликација со соодветната селекција на компанијата во делот "Show data" добивате информации за тоа
                    како се движеле нивните акции во изминатава деценија.

                    За да ги видите податоците, по кликањето врз името на соодветната компанија, скролајте надолу
                    по што ќе ви биде отворена табела со информации.


                </p>
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
