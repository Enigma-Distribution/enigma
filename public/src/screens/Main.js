import { Grid } from '@mui/material';
import React, { useEffect, useState } from 'react';
import CardComponent from '../components/CardComponent';
import CreateTaskBlock from '../components/CreateTaskBlock';
import NavbarComponent from '../components/NavbarComponent';
import Container from '@mui/material/Container';
import { Box } from '@mui/system';
import axios from 'axios';
import { useHistory } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { SERVER_BASE_URL } from '../constants';

function Main(props) {

  const [tasks, setTasks] = useState([])
  const history = useHistory()
  const dispatch = useDispatch()

  
  useEffect(() => {
    const dataForApi = {}
  
    const headers = {
      token: props.user.TOKEN || localStorage.getItem("TOKEN") 
    }
    axios.post(`${SERVER_BASE_URL}/alltasks`, dataForApi, {headers})
    .then(response => {
      console.log(response)
      const { STATUS, MSG, DATA } = response.data
      if(STATUS == "FAIL") {
        alert(MSG)
      }
      else if(STATUS == "OK") {
        console.log("DATA")
        console.log(DATA)
        setTasks(DATA)
      }
      
    }).catch(() => {
      dispatch({ type: "SET_USER", payload: null });
      localStorage.removeItem("USER")
    });
  },[])

  // if(!localStorage.getItem("TOKEN")) {
  //   history.pushState("/login")
  //   return <div>
  //     Loading...
  //   </div>
  // }

  return (
    <div>
      
      <Box sx={{ flexGrow: 1 }}>
      
      <CreateTaskBlock />
      
        <h2>Tasks: ({tasks.length})</h2>
        <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}>
          {tasks.map((task, index) => (
            <Grid item xs={12} sm={4} md={4} key={index}>
              <div style={{ padding:"20px" }}>
                <CardComponent task={task} />
              </div>
            </Grid>
          ))}
        </Grid>
      </Box>

    </div>

  );
}


export default Main;
