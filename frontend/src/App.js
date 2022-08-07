import './App.css';
import { Grid } from '@material-ui/core';
import Header from './components/Header';
import PostContent from './components/PostContent'
import About from './components/About';
import SearchForm from './components/SearchForm';
import TabList from './components/TabList';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles ({
  form_margin: {
    margin: '20px 0px',
    align: 'center'
  },
});

function App() {
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
              <Route path="/" element={<TabList />} />
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