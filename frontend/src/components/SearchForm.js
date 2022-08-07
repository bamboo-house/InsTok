import React from 'react'
import Search from '@material-ui/icons/Search';
import { makeStyles } from '@material-ui/core/styles';
import { TextField, Button } from '@material-ui/core';


const useStyles = makeStyles ({
  form_margin: {
    margin: '20px 20px',
  },
  margin: {
    margin: '5.5px 0 0 12px',
  },
  margin_left: {
    padding: '0 0 0 45',
  }
});


function SearchForm() {
  const classes = useStyles();

  // handleSubmit(e) {
  //   alert('Alertalertalert');
  //   e.preventDefault();
  // }
  
  return (
    <form className={classes.margin_left} >
      <TextField id="outlined-basic" label="Search" variant="outlined" />
      <Button variant="contained" color="primary" endIcon={<Search/>} size="large" className={classes.margin} >検索</Button>
    </form>
  );
}

export default SearchForm