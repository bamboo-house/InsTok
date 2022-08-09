import './App.css';
import { Grid } from '@material-ui/core';
import Header from './components/Header';
import PostContent from './components/PostContent'
import About from './components/About';
import TabList from './components/TabList';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { makeStyles } from '@material-ui/core/styles';
import axios from 'axios';
import React, { useState } from 'react';
import { useForm } from "react-hook-form";
import { TextField, Button } from '@material-ui/core';
import Search from '@material-ui/icons/Search';



const useStyles = makeStyles ({
  form_margin: {
    margin: '20px 0px',
    align: 'center'
  },

  margin: {
    margin: '5.5px 0 0 12px',
  },
});

let renderCount = 0;

function App() {
  const [post, setPosts] = useState([])
  const classes = useStyles();
  const { register, handleSubmit } = useForm();

  const onSubmitt = (word, e) => {
    axios.get("http://127.0.0.1:8000/api/tiktok_api/" + word.word)
    .then(res => {
      setPosts(res.data)
    });
    e.preventDefault();
  }

  return (
    <Grid container direction="column">
      <Grid item>
        <Header />
      </Grid>

      <Grid container>
        <Grid item xs={4}/>
        <Grid item xs={4} className={classes.form_margin}>
          <form onSubmit={handleSubmit(onSubmitt)}>
            <TextField id="outlined-basic" label="Search" variant="outlined" {...register("word")} />
            <Button variant="contained" type='sumbit' color="primary" endIcon={<Search/>} size="large" className={classes.margin} >検索</Button>
          </form> 
        </Grid>
        <Grid item xs={4}/>
      </Grid>

      <Grid container>
        <Grid item sm={2}/>
        <Grid item xs={12} sm={8}>
          <Router>
            <Routes>
              <Route path="/" element={<TabList post={post}/>} />
              <Route path="/post/:id" element={<PostContent />} />
              <Route path="/about" element={<About />} />
            </Routes>
          </Router>
        </Grid>
        <Grid item sm={1}/>
      </Grid>

    </Grid>
  );
}

export default App;