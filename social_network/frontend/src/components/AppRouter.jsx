import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Users from "../pages/Users";
import News from "../pages/News";
import Comments from "../pages/Comments";
import Signup from "../pages/Signup";
import Login from "../pages/Login";
import Header from "./Header";
import User from "../pages/User";
import Item from "../pages/Item";

const AppRouter = () => {
    return (
        <Router>
            <Header />
            <Routes>
                <Route path={"/users"} element={<Users />} />
                <Route path={"users/:userId"} element={<User />} />
                <Route path={"/news"} element={<News />} />
                <Route path={"/news/:newsId"} element={<Item />} />
                <Route path={"/comments"} element={<Comments />} />
                <Route path={"/signup"} element={<Signup />} />
                <Route path={"/login"} element={<Login />} />
            </Routes>
        </Router>
    );
};

export default AppRouter;