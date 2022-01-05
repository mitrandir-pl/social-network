import React, {useState} from 'react';
import Users from './components/Users'
import News from './components/News'
import Comments from './components/Comments';

function App() {
  const [posts, setPosts] = useState([
        {username: 'user1', email: 'aadada'},
        {username: 'user2', email: 'bbbbb'},
        {username: 'user3', email: 'ccccc'}
      ]
  )
  return (
      <div>
        <Users />
        <News />
        <Comments />
      </div>
      // <div>
      //     {posts.map((post) =>
      //         <h1 key={post.username}>Hello</h1>
      //     )}
      // </div>
  );
}

export default App;
