import React, {Component} from 'react';

class Comments extends Component {

    constructor(props) {
        super(props);
        this.state = {
            items: [],
            isLoaded: false,
        }
    }

    componentDidMount() {
        fetch('http://127.0.0.1:8000/api/v1/comments/')
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
                                Title: {item.post}
                                Author: {item.author}
                                Content: {item.content}
                            </li>
                        ))}
                    </ul>
                </div>
            )
        }
    }
}

export default Comments;
