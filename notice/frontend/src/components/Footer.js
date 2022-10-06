import React from "react";


const Footer = () => {
    const footerStyle = {
        height: 100,
        width: '100%',
        bottom: 0,
        margin: 0,
        backgroundColor: '#2c98bc',
        color: 'white',
        textAlign: 'center',
        position: 'absolute',
    }

    return (
        <footer style={footerStyle}>
            <p>2022</p>
        </footer>
    );
};
export default Footer;