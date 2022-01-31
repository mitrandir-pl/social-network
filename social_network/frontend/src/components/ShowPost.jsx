import * as React from 'react';
import {useNavigate} from 'react-router-dom';
// import {makeStyles} from '@mui/styles';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';


function ShowPost(props) {

  const navigate = useNavigate();

  const watchCurrentPost = () => {
    console.log('!!!!!!!')
    navigate(`/news/${props.post.id}`, {name: props.post.title });
  }

  return (
    <Card sx={{
      maxWidth: '100%',
      backgroundColor: '#f9f3c5',
    }}>
      <CardMedia
        component="img"
        alt="green iguana"
        height="540"
        image={props.post.image}
      />
      <CardContent>
        <Typography gutterBottom
                    variant="h5"
                    component="div"
                    sx={{ color: '#646f6f'}}>
          {props.post.title}
        </Typography>
        <Typography variant="body2"
                    sx={{ color: '#646f6f'}}>
          Lizards are a widespread group of squamate reptiles, with over 6,000
          species, ranging across all continents except Antarctica
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small"
                variant="contained"
                sx={{
                  backgroundColor: '#e9e581',
                  color: '#646f6f',
                  '&:hover': {
                    backgroundColor: '#fff',
                    color: '#646f6f',
                  }
                }}>
          Share
        </Button>
        <Button size="small"
                variant="contained"
                sx={{
                  backgroundColor: '#e9e581',
                  color: '#646f6f',
                  '&:hover': {
                  backgroundColor: '#fff',
                  color: '#646f6f',
                  }
                }}
                onClick={watchCurrentPost}>
          Learn More
        </Button>
      </CardActions>
    </Card>
  );
};

export default ShowPost;
