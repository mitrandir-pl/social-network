import React, {useState, useEffect} from 'react';
import {Link, useParams} from "react-router-dom";
import axios from "axios";

function Item() {

    const [item, setItem] = useState(null);
    const params = useParams();

    useEffect(() => {
        const apiUrl = `http://127.0.0.1:8000/api/v1/news/${params.newsId}`;
        axios.get(apiUrl).then((response) => {
            setItem(response.data);
        });
    }, []);

    if (!item) return <h1>Loading...</h1>;

    return (
        <div>
            <button><Link to="/news">Go back</Link></button>
            <ul>
                <li>Title: {item.title}</li>
                <li>Author: {item.author}</li>
                <li>Created: {item.created}</li>
                <li>Content: {item.content}</li>
            </ul>
        </div>
    );
}

export default Item;