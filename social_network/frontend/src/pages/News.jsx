import React, {Component} from 'react';
import api from "../components/Axios";
import {Link} from 'react-router-dom';

class News extends Component {

    constructor(props) {
        super(props);
        this.state = {
            items: [],
            isLoaded: false,
        }
    }

    componentDidMount() {
        api.get('http://127.0.0.1:8000/api/v1/news/')
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
                                    <li>Title: <Link
                                        to={`/news/${item.id}`}
                                        state={{name: item.title}}
                                    > {item.title} </Link>
                                    </li>
                                    <li>Author: {item.author}</li>
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
