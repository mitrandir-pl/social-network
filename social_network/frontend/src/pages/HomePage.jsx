import React, {useState, useEffect} from 'react';
import api from "../components/Axios"
import {Link} from "react-router-dom";

function HomePage(){

    const username = localStorage.getItem('username');
    const [news, setNews] = useState(null);

    useEffect(() => {
        const apiUrl = 'http://127.0.0.1:8000/api/v1/news/my_news/';
        api.post(apiUrl, {author: username})
            .then((response) => {
            setNews(response.data);
        });
    }, []);

    if (!news) return <h1>Loading...</h1>;

    return (
        <div>
            <Link to="/create" className="button1">Create post</Link>
            {news.map(item => (
                <li key={item.id}>
                    <ul>
                        <li>Title: <Link
                            to={`/news/${item.id}`}
                            state={{name: item.title}}
                        > {item.title} </Link></li>
                        <li>Author: {item.author}</li>
                        <li>Created: {item.created}</li>
                    </ul>
                </li>
            ))}
        </div>
    );
}

export default HomePage;