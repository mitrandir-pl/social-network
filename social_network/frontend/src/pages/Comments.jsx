import React, {Component} from 'react';
import api from "../components/Axios";

class Comments extends Component {

    constructor(props) {
        super(props);
        this.state = {
            items: [],
            isLoaded: false,
        }
    }

    componentDidMount() {
        api.get('http://127.0.0.1:8000/api/v1/comments/')
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
                                    <li>Title: {item.post}</li>
                                    <li>Author: {item.author}</li>
                                    <li>Content: {item.content}</li>
                                </ul>
                            </li>
                        ))}
                    </ul>
                </div>
            )
        }
    }
}

export default Comments;
