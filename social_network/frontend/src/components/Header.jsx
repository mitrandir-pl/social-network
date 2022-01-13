import React from 'react';
import {Link} from 'react-router-dom';
import "../CSS/header.css";

function Header() {
    return (
        <div>
            <Link to="/users" className="button1">Users</Link>
            <Link to="/news" className="button1">News</Link>
            <Link to="/comments" className="button1">Comments</Link>
            <Link to="/login" className="button1">Login</Link>
            <Link to="/signup" className="button1">Register</Link>
        </div>
    );
}

export default Header;
