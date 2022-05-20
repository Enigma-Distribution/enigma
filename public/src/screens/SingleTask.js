import { Button, Card, CardActions, CardContent, Container, LinearProgress, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Typography } from '@mui/material';
import { Box } from '@mui/system';
import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios'
import CardComponent from '../components/CardComponent';
import { useDispatch } from 'react-redux';
import Loading from '../components/Loading';
import { SERVER_BASE_URL } from '../constants';

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
    console.log("Insingle task, printing headers")
    console.log(headers)
    // Request 1
    axios.post(`${SERVER_BASE_URL}/task?task_id=${id}`, {}, {headers})
    .then(response => {
      const { STATUS, MSG, TASK } = response.data
      console.log(response)
      if(STATUS == "FAIL") {
        console.log("Request 1 to get task failed")
        alert(MSG)
      }
      else if(STATUS == "OK") {
        console.log("Received task", TASK)
        setTask(TASK)
      }

      // Request 2
      axios.post(`${SERVER_BASE_URL}/task/get_task_meta_data?task_id=${id}`, {}, {headers})
      .then(response => {
        const { STATUS, MSG, STEPS } = response.data
        console.log(response)
        if(STATUS == "FAIL") {
          console.log("Request 2 to get task failed")
          alert(MSG)
        }
        else if(STATUS == "OK") {
          console.log("Received steps")
          setSteps(STEPS)
          console.log("STATUS:OK")
        }
        
      }).catch((e) => {
        console.log(e)
        dispatch({ type: "SET_USER", payload: null });
        localStorage.removeItem("USER")
      });

      
    }).catch((e) => {
      console.log(e)
      // dispatch({ type: "SET_USER", payload: null });
      // localStorage.removeItem("USER")
    });


  },[])

  if(!task){
    return <Loading />
  }

  // how many steps are completed
  let steps_stats = {
    map_count: 0,
    shuffle_count: 0,
    reduce_count: 0,
    COMPLETED_count: 0,
    count_of_all_steps_with_all_phases: steps.length*3,
    completed_phases: 0
  }
  for(var i=0; i< steps.length;i++){
    if(steps[i].phase == "map"){
      steps_stats["map_count"] += 1
    }
    else if(steps[i].phase == "shuffle"){
      steps_stats["shuffle_count"] += 1
      steps_stats["completed_phases"] += 1
    }
    else if(steps[i].phase == "reduce"){
      steps_stats["reduce_count"] += 1
      steps_stats["completed_phases"] += 2
    }
    else if(steps[i].phase == "COMPLETED"){
      steps_stats["COMPLETED_count"] += 1
      steps_stats["completed_phases"] += 3
    }
  }

  const percent_completed = 100*(steps_stats["completed_phases"]/steps_stats["count_of_all_steps_with_all_phases"])

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
      <h2>Task Status: {task.task_status ? <span style={{color:"green"}}>Completed</span> : "Not Completed"}</h2>   
      
      {task.result_file_id && task.task_status && <div>
        Checkout result on <a href={`/resulttable/${task.result_file_id}`}>Result</a>
        <br></br>
        Result File: {"  "}  
        <a href={`https://ipfs.infura.io/ipfs/${task.result_file_id}`}>{`https://ipfs.infura.io/ipfs/${task.result_file_id}`}</a>
      </div>}   

      <br></br>
        
        <div>
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                
                <TableCell align="center"><b>Steps in Map</b></TableCell>
                <TableCell align="center"><b>Steps in Shuffle</b></TableCell>
                <TableCell align="center"><b>Steps in Reduce</b></TableCell>
                <TableCell align="center"><b>COMPLETED</b></TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              
                <TableRow
                  key={"row.name"}
                  sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                >
                  {/* <TableCell component="th" scope="row">
                    {row.name}
                  </TableCell> */}
                  <TableCell align="center">{steps_stats["map_count"]}</TableCell>
                  <TableCell align="center">{steps_stats["shuffle_count"]}</TableCell>
                  <TableCell align="center">{steps_stats["reduce_count"]}</TableCell>
                  <TableCell align="center">{steps_stats["COMPLETED_count"]}</TableCell>
                </TableRow>
              
            </TableBody>
          </Table>
        </TableContainer>
        </div>


      <h2>Progress</h2>
      <LinearProgressWithLabel value={percent_completed} />


      <br></br>
      <h2>Zip file link</h2>
      <a href={`https://ipfs.infura.io/ipfs/${task.task_zip_file_id}`}>{`https://ipfs.infura.io/ipfs/${task.task_zip_file_id}`}</a>

      <br></br><br></br>
      <h2>Sub Tasks - {steps.length}</h2>
      {steps.map((s) => {
      let completed_step_green_border = { margin:"20px", borderWidth:"2px", borderStyle:"solid", borderColor:"green" }
      let normal_border = { margin:"20px", borderWidth:"2px"}  
      return (
          <div id={s.step_id} style={s.is_completed == 1 ? completed_step_green_border : normal_border}>

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
                <Typography variant="body2">
                step_created_ts: {s.step_created_ts ? s.step_created_ts : "NA"} 
                </Typography>
                <Typography variant="body2">
                step_updated_ts: {s.step_updated_ts ? s.step_updated_ts : "NA"} 
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
