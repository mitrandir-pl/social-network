// import React from 'react';
//
// function Header() {
//     return (
//         <div>
//             <Link to="/users" className="button1">Users</Link>
//             <Link to="/news" className="button1">News</Link>
//             <Link to="/comments" className="button1">Comments</Link>
//             <Link to="/home" className="button1">Home</Link>
//             <Link to="/login" className="button1">Login</Link>
//             <Link to="/signup" className="button1">Register</Link>
//         </div>
//     );
// }
//
// export default Header;

import * as React from 'react';
import {Link, useNavigate} from 'react-router-dom';
import { Navigate } from 'react-router';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';

export default function ButtonAppBar() {

  const navigate = useNavigate();
  const login = () => {
    navigate("/login");
  }
  const signup = () => {
    navigate("/signup")
  }

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            News
          </Typography>
          <ButtonGroup variant="contained" aria-label="outlined button group">
            <Button color="primary" onClick={login}>SignIn</Button>
            <Button color="secondary" onClick={signup}>SignUp</Button>
          </ButtonGroup>
        </Toolbar>
      </AppBar>
    </Box>
  );
}
