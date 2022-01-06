import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import axios from "axios";


class Users extends Component {


    constructor(props) {
        super(props);
        this.state = {
            items: [],
            isLoaded: false,
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/v1/users/')
            .then(res => {
                const items = res.data;
                this.setState({
                    items,
                    isLoaded: true
                });
            })
    }

    render() {
        let {isLoaded, items} = this.state;
        if(!isLoaded) {
            return <div>Loading...</div>
        }
        else {
            return (
                <div>
                    <ul>
                        {items.map(item => (
                            <li key={item.id}>
                                <ul>
                                    <li>Username: <Link to={`/users/${item.id}`}>{item.username}</Link></li>
                                </ul>
                            </li>
                        ))}
                    </ul>
                </div>
            )
        }
    }
}

export default Users;
