import React, { useEffect, useState } from 'react';
import BodyCard from './BodyCard'
import { Grid } from '@material-ui/core'
import axios from 'axios';

const cardContent = {
  avatarUrl: "https://joeschmoe.io/api/v1/random",
}

function Content() {
  const [post, setPosts] = useState([])

  useEffect(() => {
    // axios.get('https://jsonplaceholder.typicode.com/posts')
    axios.get('http://127.0.0.1:8000/api/instagram_api/')
    .then(res => {
      setPosts(res.data)
    })
  }, [])

  const getCardContent = getObj => {
    const bodyCardContent = {...getObj, ...cardContent};
    return (
      <Grid item xs={12} sm={4} key={getObj.id}>
        <BodyCard {...bodyCardContent} />
      </Grid>
    );
  };

  return (
    <Grid container spacing={2}>
      {post.map(contentObj => getCardContent(contentObj))}
    </Grid>
  );
}

export default Content