import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
// import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import axios from 'axios'
import { useHistory } from "react-router-dom";
import { useDispatch } from 'react-redux';
import { SERVER_BASE_URL } from '../constants';

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="https://mui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const theme = createTheme();

export default function Register() {

  const [formErrors, setFormErrors] = React.useState([])
  let history = useHistory();
  const dispatch = useDispatch()

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    // eslint-disable-next-line no-console

    // if (){
    //   alert("Fill al the fields")
    // }
    
    const dataForApi = {
      username: data.get('userName'),
      email: data.get('email'),
      password: data.get('password'),
      user_type: "user"
      // user_type: "worker",
      // upi_id:"rugved@upi"
    }

// EMAIL: "rugvedworker@gmail.com"
// TOKEN: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJVU0VSX0lEIjoiZjFkZjU2ZjYtYzQxOC00YTgxLTg1MDItNjE5Mjg5ZThlYzk3IiwiZXhwIjoxNjQ3Nzg5MzAxfQ.P_eNKNhYq8VLxEhXOke40QqSPI18_4cg7Y2XTyaEg7E"
// USERNAME: "rugvedworker"

    axios.post(`${SERVER_BASE_URL}/authenticate/user/new`, dataForApi)
        .then(response => {
          console.log(response)
          const { STATUS, MSG, TOKEN } = response.data
          if(STATUS == "FAIL") {
            setFormErrors([MSG])
            console.log(MSG)
          }
          else if(STATUS == "OK") {
            const { USERNAME, EMAIL } = response.data
            // localStorage.setItem("TOKEN", TOKEN)
            // localStorage.setItem("USER", JSON.stringify({ USERNAME, EMAIL, TOKEN }))
            // dispatch({type: "SET_USER", payload: { USERNAME, EMAIL, TOKEN }})
            // setTimeout(() => history.push("/main"), 1000)
            history.push("/login")
          }
          
        })
        .catch(err => history.push("/login"));

  };

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1}}>
          <img src="/icon.png" style={{ width: "100%", height: "auto" }} />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign up
          </Typography>
          <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
          <div>
            {formErrors.map(e => {
              return <p>{e}</p>
            })}
          </div>
            <Grid container spacing={2}>
              <Grid item xs={12}>
                <TextField
                  autoComplete="given-name"
                  name="userName"
                  required
                  fullWidth
                  id="userName"
                  label="Username"
                  autoFocus
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="email"
                  label="Email Address"
                  name="email"
                  autoComplete="email"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name="password"
                  label="Password"
                  type="password"
                  id="password"
                  autoComplete="new-password"
                />
              </Grid>
              {/* <Grid item xs={12}>
                <FormControlLabel
                  control={<Checkbox value="allowExtraEmails" color="primary" />}
                  label="I want to receive inspiration, marketing promotions and updates via email."
                />
              </Grid> */}
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign Up
            </Button>
            <Grid container justifyContent="flex-end">
              <Grid item>
                <Link href="login" variant="body2">
                  Already have an account? Sign in
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
        <Copyright sx={{ mt: 5 }} />
      </Container>
    </ThemeProvider>
  );
}