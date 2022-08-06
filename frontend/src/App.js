import './App.css';
import { Grid } from '@material-ui/core';
import Header from './components/Header'

function App() {
  return (
    <Grid container direction="column">
      <Grid item>
        <Header />
      </Grid>
      <Grid item container>
        <Grid sm={2}/>
        <Grid xs={12} sm={8}>
          item1item1item1item1item1item1item1item1item1item1item1item1
          item1item1item1item1item1item1item1item1item1item1item1item1item1item1item1item1item1item1item1item1item1item1item1item1
          item1item1item1item1item1item1item1item1item1item1item1item1
          item1item1item1item1item1item1item1item1item1item1item1item1
        </Grid>
        <Grid sm={2}/>
      </Grid>
    </Grid>
  );
}

export default App;