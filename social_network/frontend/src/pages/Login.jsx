import React, {useState} from "react";
import {useNavigate} from "react-router-dom";
import api from "../components/Axios";
import axios from "axios";
import "../CSS/login.css";

function Login() {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const submit = (event) => {
        event.preventDefault();
        const apiUrl = "http://127.0.0.1:8000/api/token/";
        axios.post(apiUrl, {
            username: username,
            password: password
        })
            .then(response => {
                if (response.status === 200) {
                    api.defaults.headers['Authorization'] = "JWT " + response.data.access;
                    localStorage.setItem('access_token', response.data.access);
                    localStorage.setItem('refresh_token', response.data.refresh);
                    localStorage.setItem('username', username);
                    navigate("/news");
                } else {
                    console.log('Something went wrong!');
                }
            });
    }

    return (
        <div className="container">
        <form onSubmit={submit}>
            <div className="input-block">
                <input name="username" placeholder="Enter username"
                    type="text" value={username}
                    onChange={event => setUsername(event.target.value)} />
                <input name="password" placeholder="Enter password"
                    type="password" value={password}
                    onChange={event => setPassword(event.target.value)} />
            </div>
            <input type="submit" value="Submit" />
            </form>
        </div>
        )
}

export default Login;
