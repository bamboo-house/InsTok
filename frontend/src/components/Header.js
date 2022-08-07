import React from 'react'
import { AppBar, makeStyles, Toolbar, Typography } from '@material-ui/core'
import EcoIcon from '@material-ui/icons/Eco';

const useStyles = makeStyles(() => ({
  typographyStyles: {
    flex: 1
  }
}));

function Header() {
  const classes = useStyles();
  return (
    <AppBar position='static'>
      <Toolbar>
        <Typography className={classes.typographyStyles}>
          InsTok
        </Typography>
        <EcoIcon/>
      </Toolbar>
    </AppBar>
  );
}

export default Header