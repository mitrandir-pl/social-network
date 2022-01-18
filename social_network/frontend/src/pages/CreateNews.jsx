import React, {useState, useEffect} from 'react';
import api from "../components/Axios";

function CreateNews() {

    const username = localStorage.getItem('username');
    const [news, setNews] = useState(null);

    useEffect(() => {
        const apiUrl = 'http://127.0.0.1:8000/api/v1/news/create/';
        api.post(apiUrl, {
            author: username})
            .then((response) => {
                setNews(response.data);
            });
    }, []);

    return (
        <div>
            Hello
        </div>
    );
};

export default CreateNews;