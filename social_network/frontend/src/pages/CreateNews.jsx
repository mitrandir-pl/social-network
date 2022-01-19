import React, {useState, useEffect} from 'react';
import api from "../components/Axios";

function CreateNews() {

    const username = localStorage.getItem('username');
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    const addNewPost = () => {
        const apiUrl = 'http://127.0.0.1:8000/api/v1/news/create/';
        api.post(apiUrl, {
            author: username,
            title: title,
            content: content
        })
    };

    return (
        <div>
            <input name="title" placeholder="Enter title"
               type="text" value={title}
                   onChange={event => setTitle(event.target.value)} />
            <input name="content" placeholder="Enter content"
                   type="text" value={content}
                   onChange={event => setContent(event.target.value)} />
            <button onClick={addNewPost}>Post</button>
        </div>
    );
}

export default CreateNews;