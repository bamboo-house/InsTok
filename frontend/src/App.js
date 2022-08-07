import './App.css';
import { Grid, TextField, Button } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

import Header from './components/Header';
import Content from './components/Content';
import PostContent from './components/PostContent'
import About from './components/About';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Search from '@material-ui/icons/Search';

const useStyles = makeStyles ({
  form_margin: {
    margin: '20px 20px',
  },
  margin: {
    margin: '5.5px 0 0 15px',
  }
});

function App() {
  const classes = useStyles();
  return (
    <Grid container direction="column">
      <Grid item>
        <Header />
      </Grid>

      <Grid container>
        <Grid item xs={5}/>
        <Grid item xs={2} className={classes.form_margin}>
          <form>
            <TextField id="outlined-basic" label="Search" variant="outlined" />
            <Button variant="contained" color="primary" endIcon={<Search/>} size="large" className={classes.margin} >検索</Button>
          </form>
        </Grid>
        <Grid item xs={5}/>
      </Grid>

      <Grid container>
        <Grid item sm={2}/>
        <Grid item xs={12} sm={8}>
          <Router>
            <Routes>
              <Route path="/" element={<Content />} />
              <Route path="/post/:id" element={<PostContent />} />
              <Route path="/about" element={<About />} />
            </Routes>
          </Router>
        </Grid>
        <Grid item sm={2}/>
      </Grid>

    </Grid>
  );
}

export default App;