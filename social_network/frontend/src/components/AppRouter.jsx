import React from 'react';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Header from "./Header";
import Users from "../pages/Users";
import News from "../pages/News";
import Comments from "../pages/Comments";
import User from "../pages/User";


const AppRouter = () => {
    return (
        <Router>
            <Header />
            <Routes>
                <Route path="/users" element={<Users />} />
                {/*<Route path="/:userId" element={<User />}*/}
                <Route path="users/:userId" element={<User />} />
                <Route path="/news" element={<News />} />
                <Route path="/comments" element={<Comments />} />
            </Routes>
        </Router>
    );
};

export default AppRouter;