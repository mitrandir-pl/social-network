import React from 'react';
import {Link} from 'react-router-dom';

function Header() {
    return (
        <div>
            <button><Link to="/users">Users</Link></button>
            <button><Link to="/news">News</Link></button>
            <button><Link to="/comments">Comments</Link></button>
        </div>
    );
}

export default Header;
