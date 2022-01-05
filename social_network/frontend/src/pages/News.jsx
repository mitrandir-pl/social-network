import React, {Component} from 'react';
import axios from 'axios';

class News extends Component {

    constructor(props) {
        super(props);
        this.state = {
            items: [],
            isLoaded: false,
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/v1/news/')
            .then(res => {
                const items = res.data;
                this.setState({
                    items,
                    isLoaded: true
                });
            })
        // fetch('http://127.0.0.1:8000/api/v1/news/')
        //     .then(res => res.json())
        //     .then(json =>{
        //         this.setState({
        //             isLoaded: true,
        //             items: json,
        //         })
        //     });
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
                                    <li>Title: {item.title}</li>
                                    <li>Author: {item.author}</li>
                                    <li>Created: {item.created}</li>
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

export default News;
