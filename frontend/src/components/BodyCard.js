import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { CardActions, Card, CardContent, Button, Typography, CardHeader, IconButton, Avatar, CardMedia } from '@material-ui/core';
import StarBorderOutlinedIcon from '@material-ui/icons/StarBorder';


const useStyles = makeStyles({
    bullet: {
      display: 'inline-block',
      margin: '0 2px',
      transform: 'scale(0.8)',
    },
    title: {
      fontSize: 14,
    },
    pos: {
      marginBottom: 12,
    },
    cHeader: {
      height: '50px',
      overflow: 'hidden',
      textOverflow: 'ellipsis',
      whiteSpace: 'nowrap',
      "& .MuiCardHeader-content": {
          overflow: 'hidden'
      }
    },
    cContent: {
        height: '200px',
        overflow: 'hidden'
    }
});


function BodyCard(props) {
  const { userId, id, title, body, avatarUrl, imageUrl } = props;
  const classes = useStyles();
  return (
      <Card variant="outlined">
      <CardHeader
          avatar={<Avatar src={avatarUrl} />}
          action={
            <IconButton aria-label="settings">
              <StarBorderOutlinedIcon />
            </IconButton>
          }
          title={title}
          className={classes.cHeader}
        />
      
      <CardMedia style={{ height: "150px" }} image={imageUrl} />
      <CardContent className={classes.cCOntent}>
        <Typography variant="body2" component="p">
          {body}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small" href={`/post/${id}`}>詳細をみる</Button>
      </CardActions>
    </Card>
  );
}

export default BodyCard
