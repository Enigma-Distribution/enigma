import { Button, Card, CardActions, CardContent, Container, LinearProgress, Typography } from '@mui/material';
import { Box } from '@mui/system';
import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios'
import CardComponent from '../components/CardComponent';
import { useDispatch } from 'react-redux';
import Loading from '../components/Loading';

function LinearProgressWithLabel(props) {
  return (
    <Box sx={{ display: 'flex', alignItems: 'center' }}>
      <Box sx={{ width: '100%', mr: 1 }}>
        <LinearProgress variant="determinate" {...props} />
      </Box>
      <Box sx={{ minWidth: 35 }}>
        <Typography variant="body2" color="text.secondary">{`${Math.round(
          props.value,
        )}%`}</Typography>
      </Box>
    </Box>
  );
}

function SingleTask(props) {
  // const { id } = useParams();
  //http://localhost:3001/task/2c8635c8-e0e9-4a2f-be12-d1d8de4e7f1e
  const id = window.location.href.split("/task/")[1]
  console.log(id);

  const [task, setTask] = React.useState()
  const [steps, setSteps] = React.useState([])
  const dispatch = useDispatch()

  useEffect(() => {
  
    const headers = {
      token: props.user.TOKEN || localStorage.getItem("TOKEN")
    }
    // Request 1
    axios.post(`http://127.0.0.1:5000/task?task_id=${id}`, {}, {headers})
    .then(response => {
      const { STATUS, MSG, TASK } = response.data
      console.log(response)
      if(STATUS == "FAIL") {
        alert(MSG)
      }
      else if(STATUS == "OK") {
        setTask(TASK)
      }
      
    }).catch((e) => {
      console.log(e)
      // dispatch({ type: "SET_USER", payload: null });
      // localStorage.removeItem("USER")
    });

    // Parallel request 2
    axios.post(`http://127.0.0.1:5000/task/get_task_meta_data?task_id=${id}`, {}, {headers})
    .then(response => {
      const { STATUS, MSG, STEPS } = response.data
      console.log(response)
      if(STATUS == "FAIL") {
        alert(MSG)
      }
      else if(STATUS == "OK") {
        setSteps(STEPS)
        console.log("STATUS:OK")
      }
      
    }).catch((e) => {
      console.log(e)
      dispatch({ type: "SET_USER", payload: null });
      localStorage.removeItem("USER")
    });


  },[])

  if(!task){
    return <Loading />
  }

  return (
    <Container>
      <h1> {task.task_name} </h1>
      <p>ID: {id}</p>
      <hr></hr>

      <h3 style={{
        fontStyle:"italic",
        fontWeight:"lighter"
      }}>{task.task_description}</h3>

      <br></br>
      <h2>Task Status: {task.task_status}</h2>      

      <br></br>
      <h2>Progress</h2>
      <LinearProgressWithLabel value={70} />


      <br></br>
      <h2>Zip file link</h2>
      <a href={`https://ipfs.infura.io/ipfs/${task.task_zip_file_id}`}>{`https://ipfs.infura.io/ipfs/${task.task_zip_file_id}`}</a>

      <br></br><br></br>
      <h2>Sub Tasks</h2>
      {steps.map((s) => {
        return (
          <div id={s.step_id} style={{ margin:"20px" }}>
            <Card>
              <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                  {s.is_completed == 0 ? "Not Completed" : "Completed"}
                </Typography>
                <Typography variant="h5" component="div">
                  {s.step_id}
                </Typography>
                <Typography sx={{ mb: 1.5 }} color="text.secondary">
                  {s.phase}
                </Typography>
                <Typography variant="body2">
                  Assigned to: {s.assigned_to ? s.assigned_to : "None"} 
                </Typography>
              </CardContent>
              <CardActions>
                <Button size="small" disabled={s.is_completed == 1 ? false : true} href={`https://ipfs.infura.io/ipfs/${s.result_file_id}`} >Check Result</Button>
              </CardActions>
            </Card>

          </div>
        )
      })}
      

    </Container>
  );
}


export default SingleTask;
