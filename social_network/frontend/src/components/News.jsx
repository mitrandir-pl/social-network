import React, {Component} from 'react';

class News extends Component {

    constructor(props) {
        super(props);
        this.state = {
            items: [],
            isLoaded: false,
        }
    }

    componentDidMount() {
        fetch('http://127.0.0.1:8000/api/v1/news/')
            .then(res => res.json())
            .then(json =>{
                this.setState({
                    isLoaded: true,
                    items: json,
                })
            });
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
                                Title: {item.title}
                                Author: {item.author}
                                Created: {item.created}
                                Content: {item.content}
                            </li>
                        ))}
                    </ul>
                </div>
            )
        }
    }
}

export default News;
