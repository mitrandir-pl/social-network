import React, {Component} from "react";
import api from "../components/Axios";
import {Link} from "react-router-dom";
import ShowPost from "../components/ShowPost";

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
                        {items.map(item => (
                            <div key={item.id}>
                                <ShowPost post={item} />
                            </div>
                        ))}
                </div>
            )
        }
    }
}

export default News;
