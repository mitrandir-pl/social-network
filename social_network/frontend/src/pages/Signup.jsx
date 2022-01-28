import React, {useState} from "react";
import axios from "axios";
import "../CSS/login.css";

function Signup() {

    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const submit = (event) => {
        event.preventDefault();
        const apiUrl = "http://127.0.0.1:8000/api/v1/users/registration";
        axios.post(apiUrl, {
            username: username,
            email: email,
            password: password,
        })
            .then(response => {
                response.status === 201
                    ? alert("User successfully registered")
                    : alert('Something went wrong!')
            });
    }

    return (
      <div className="container">
          <form onSubmit={submit}>
              <div className="input-block">
                  <input name="username" placeholder="Enter username"
                         type="text" value={username}
                         onChange={event => setUsername(event.target.value)} />
                  <input name="email" placeholder="Enter email"
                         type="text" value={email}
                         onChange={event => setEmail(event.target.value)} />
                  <input name="password" placeholder="Enter password"
                         type="password" value={password}
                         onChange={event => setPassword(event.target.value)} />
              </div>
              <input type="submit" value="Submit" />
          </form>
      </div>
    )
}

export default Signup;
