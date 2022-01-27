import React, { Component } from "react";
import "../CSS/login.css";
import api from "../components/Axios";

class Signup extends Component{
    constructor(props){
        super(props);
        this.state = {
            username: "",
            password: "",
            email:""
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    handleSubmit(event) {
        event.preventDefault();
        const apiUrl = "http://127.0.0.1:8000/api/v1/users/registration";
        api.post(apiUrl, {
            username: this.state.username,
            email: this.state.email,
            password: this.state.password,
        })
            .then(response => {
                response.status === 201
                    ? alert("User successfully registered")
                    : alert('Something went wrong!')
            });
    }

    render() {
        return (
            <div className="container">
                <form onSubmit={this.handleSubmit}>
                    <input name="username" placeholder="Enter username" type="text" value={this.state.username} onChange={this.handleChange}/>
                    <br/>
                    <input name="email" placeholder="Enter email" type="email" value={this.state.email} onChange={this.handleChange}/>
                    <br/>
                    <input name="password" placeholder="Enter password" type="password" value={this.state.password} onChange={this.handleChange}/>
                    <br/>
                    <input type="submit" value="Submit"/>
                </form>
            </div>
        )
    }
}
export default Signup;