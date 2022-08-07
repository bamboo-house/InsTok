import './App.css';
import { Grid } from '@material-ui/core';
import Header from './components/Header';
import PostContent from './components/PostContent'
import About from './components/About';
import SearchForm from './components/SearchForm';
import TabList from './components/TabList';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { makeStyles } from '@material-ui/core/styles';
import axios from 'axios';
import React, { useEffect, useState } from 'react';


const useStyles = makeStyles ({
  form_margin: {
    margin: '20px 0px',
    align: 'center'
  },
});

function App() {
  const [post, setPosts] = useState([])

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/instagram_api/')
    .then(res => {
      setPosts(res.data)
    })
  }, [])

  const classes = useStyles();
  return (
    <Grid container direction="column">
      <Grid item>
        <Header />
      </Grid>

      <Grid container>
        <Grid item xs={4}/>
        <Grid item xs={4} className={classes.form_margin}>
          <SearchForm />
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