import React from "react";
import {Link} from 'react-router-dom'


const Menu = () => {
    const menuStyle = {
        padding: 0,
        margin: 0,
        height: 100,
        backgroundColor: '#2c98bc',
        color: 'white',
        textAlign: 'center',
    }

    return (
        <menu style={menuStyle}>
            <ul>
                <li><Link to="/">Users</Link></li>
                <li><Link to="/project">Projects</Link></li>
                <li><Link to="/todo">Tasks</Link></li>
            </ul>
        </menu>
    );
};
export default Menu;