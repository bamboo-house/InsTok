import React, { useEffect, useState } from 'react';
import BodyCard from './BodyCard'
import { Grid } from '@material-ui/core'
import axios from 'axios';

const cardContent = {
  avatarUrl: "https://joeschmoe.io/api/v1/random",
}

const getCardContent = getObj => {
  const bodyCardContent = {...getObj, ...cardContent};
  return (
    <Grid item xs={12} sm={4} key={getObj.id}>
      <BodyCard {...bodyCardContent} />
    </Grid>
  );
};

function Content(props) {
  const post = props.post
  return (
    <Grid container spacing={2}>
      {post.map(contentObj => getCardContent(contentObj))}
    </Grid>
  );
}

export default Content