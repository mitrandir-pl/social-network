import React, {useState, useEffect} from 'react';
import {Link, useParams, useLocation} from "react-router-dom";
import api from "../components/Axios";

function Item() {

    const username = localStorage.getItem('username');
    const [item, setItem] = useState({});
    const [comment, setComment] = useState('');
    const [comments, setComments] = useState([]);
    const params = useParams();
    const location = useLocation();
    const post_name = location.state.name;

    useEffect(() => {
        const apiUrl = 'http://127.0.0.1:8000/api/v1/';
        api.get(apiUrl + `news/${params.newsId}`)
            .then((response) => { setItem(response.data); });
        api.post(apiUrl + 'comments/curr_post/', {post: post_name})
            .then((response) => { setComments(response.data); });
    }, []);

    const addNewComment = () => {
        const apiUrl = 'http://127.0.0.1:8000/api/v1/comments/create/';
        api.post(apiUrl, {
            author: username,
            post: post_name,
            content: comment
        });
    };

    const loc = () => {
        console.log(location.state);
    }

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
            <p>Comments: {comments.length}</p>
            <ul>
                {comments.map(comment => (
                    <li key={comment.id}>
                        <ul>
                            <li>Title: {comment.post}</li>
                            <li>Author: {comment.author}</li>
                            <li>Content: {comment.content}</li>
                        </ul>
                        <br/>
                    </li>
                ))}
            </ul>
            <input name="comment" placeholder="Enter comment"
                   type="text" value={comment}
                   onChange={event => setComment(event.target.value)} />
            <button onClick={addNewComment}>Post comment</button>
        </div>
    );
}

export default Item;