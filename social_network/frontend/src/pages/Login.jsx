import React, { Component } from "react";
import axios from "axios";
import api from "../components/Axios";
import "../CSS/login.css";

class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {username: "", password: ""};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    handleSubmit(event) {
        event.preventDefault();
        const apiUrl = "http://127.0.0.1:8000/api/token/";
        axios.post(apiUrl, {
            username: this.state.username,
            password: this.state.password
        })
            .then(response => {
                if (response.status === 200) {
                    api.defaults.headers['Authorization'] = "JWT " + response.data.access;
                    localStorage.setItem('access_token', response.data.access);
                    localStorage.setItem('refresh_token', response.data.refresh);
                    localStorage.setItem('username', this.state.username);
                } else {
                    console.log('Something went wrong!');
                }
            });
    }

    render() {
        return (
            <div className="container">
                <form onSubmit={this.handleSubmit}>
                    <div className="input-block">
                        <input name="username" placeholder="Enter username"
                               type="text" value={this.state.username}
                               onChange={this.handleChange} />
                        <input name="password" placeholder="Enter password"
                               type="password" value={this.state.password}
                               onChange={this.handleChange} />
                    </div>
                    <input type="submit" value="Submit"/>
                </form>
            </div>
        )
    }
}
export default Login;
