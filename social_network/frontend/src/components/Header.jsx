import * as React from 'react';
import {useNavigate} from 'react-router-dom';
import {makeStyles} from '@mui/styles';
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
      <AppBar position="static"
              sx={{backgroundColor: '#87aab9'}}>
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            aria-label="menu"
            sx={{
              mr: 2,
              color: '#646f6f',
            }}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6"
                      component="div"
                      sx={{
                        flexGrow: 1,
                        color: '#646f6f',
                      }}>
            Blog
          </Typography>
          <ButtonGroup variant="contained"
                       aria-label="outlined button group">
            <Button onClick={login}
                    sx={{
                      backgroundColor: '#f9f3c5',
                      color: '#646f6f',
                      height: 40,
                      padding: '0 30px',
                      fontSize: '100%',
                      fontWeight: 'bold',
                      '&:hover': {
                        backgroundColor: '#fff',
                        color: '#646f6f',
                      }
                    }}>
              SignIn
            </Button>
            <Button onClick={signup}
                    sx={{
                      backgroundColor: '#de1b1b',
                      color: 'white',
                      height: 40,
                      padding: '0 30px',
                      fontSize: '100%',
                      fontWeight: 'bold',
                      '&:hover': {
                        backgroundColor: '#fff',
                        color: '#646f6f',
                      }
                    }}>
              SignUp
            </Button>
          </ButtonGroup>
        </Toolbar>
      </AppBar>
    </Box>
  );
}

