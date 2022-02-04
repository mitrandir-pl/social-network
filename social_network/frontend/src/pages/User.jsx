import React, {useState, useEffect} from 'react';
import {Link, useParams} from "react-router-dom";
import api from "../components/Axios";

function User() {

    const [user, setUser] = useState(null);
    const params = useParams();

    useEffect(() => {
        const apiUrl = `http://127.0.0.1:8000/api/v1/users/${params.userId}`;
        api.get(apiUrl).then((response) => {
            setUser(response.data);
        });
    }, []);

    if (!user) return <h1>Loading...</h1>;

    return (
        <div>
            <button><Link to="/users">Go back</Link></button>
            <ul>
                <li>Username: {user.username}</li>
                <li>Email: {user.email}</li>
                <li>Role: {user.role}</li>
            </ul>
        </div>
    );
}


export default User
