import { Button, Input, Paper, TextField } from '@mui/material';
import axios from 'axios';
import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { create, globSource } from 'ipfs-http-client'
import Loading from '../components/Loading';
import { SERVER_BASE_URL } from '../constants';


const client = create("https://ipfs.infura.io:5001/api/v0");


function TaskForm(props) {

  const headers = {
    token: props.user.TOKEN || localStorage.getItem("TOKEN")
  }  

  const [taskName, setTaskName] = useState("")
  const [taskDescription, setTaskDescription] = useState("")
  const [zipFile, setZipFile] = useState()
  const [textFile, setTextFile] = useState()
  const[loading, setLoading] = useState(false)
  
  let history = useHistory();

  const getZipFileId = async (f) => {
    
    const formData = new FormData();
    formData.append("file", f);
    formData.append("task_file", false);
    

    // Uncomment this and replace AAAAAA in below line with actual API
    const response = await axios.post(`${SERVER_BASE_URL}/upload-file`, formData, {headers})
      
    console.log(response)
    const { STATUS, MSG, file_id } = response.data
    if(STATUS == "FAIL") {
      alert(MSG)
      return ""
    }
    else if(STATUS == "OK") {
      return file_id 
    }
  }

  function blobToFile(theBlob, fileName){       
    return new File([theBlob], fileName, { lastModified: new Date().getTime(), type: theBlob.type })
  }

  const createMiniFiles = (file = textFile,cSize = 1024*1000/* cSize should be byte 1024*1000 = 1MB */) => {
    let startPointer = 0;
    let endPointer = file.size;
    let files = [];
    while(startPointer < endPointer){
     let newStartPointer = startPointer + cSize;
     let curr_chunk = file.slice(startPointer, newStartPointer, "text/plain")
    
    files.push(blobToFile(curr_chunk, "fileName-"+ (new Date().getTime()).toString()))
    
    startPointer = newStartPointer;
  }
    
    
    return files
}


  const uploadFile = async (fileArr, wrapWithDirectory = false) => {
    console.log(fileArr)
    let respArr = []
    
    // const respArr = await client.addAll(fileArr, { progress: (prog) => console.log(`received: ${prog}`) })
    
    let base = 0
    // fileArr.slice(base,base+50)
    for await (const file of client.addAll(fileArr)) {
      // console.log(file)
      respArr.push(file)
    }  
    // console.log(respArr)

    return respArr
  }

  const submitForm = async (e) => {
    // Validation start
    if(taskName.trim() === ""){
      alert("Task name field cannot be empty")
      return
    }
    if(taskDescription.trim() === ""){
      alert("Task description field cannot be empty")
      return
    }
    if(!zipFile){
      alert("Zip file field cannot be empty")
      return
    }
    if(!textFile){
      alert("Text file field cannot be empty")
      return
    }
    
    // Validation end

    setLoading(true)
    const files = createMiniFiles(textFile)

    // console.log(files)
    // return

    const respArrTxtFiles = await uploadFile(files)
    const respArrZipFile = await uploadFile([zipFile], true)

    console.log("respArrTxtFiles")
    console.log(respArrTxtFiles)
    console.log("respArrZipFile")
    console.log(respArrZipFile)


    // const task_zip_file_id = await getZipFileId(zipFile)
    // console.log(task_zip_file_id)
    // task_zip_file_id -> pass cid of zip file

    const datasource_all_cids = respArrTxtFiles.map(d => {
      return {
        step_cid: d.path,
        step_size: d.size
      }
    })
    
    const formData = new FormData();
    // formData.append("datasource", textFile);
    formData.append("task_name", taskName);
    formData.append("task_description", taskDescription);
    formData.append("task_zip_file_id", respArrZipFile[0].path); // Cid of zip file
    formData.append("datasource_all_cids", JSON.stringify(datasource_all_cids));
    formData.append("datasource_size", textFile.size) // Total size of text file 
    // formData.append("datasource_all_cids_only", datasource_all_cids_only)
    
    axios.post(`${SERVER_BASE_URL}/newtask`, formData, {headers})
    .then(response => {
      console.log(response)
      const { STATUS, MSG, TASK } = response.data
      if(STATUS == "FAIL") {
        alert(MSG)
      }
      else if(STATUS == "OK") {
        console.log("TASK")
        console.log(TASK)
        // alert(JSON.stringify(TASK))
        history.push("/task/"+TASK.task_id)
        // history.push('/main')
      }
      
    });
    

  }


  
    const onTextFileChange = (e) => {
      console.log(e.target.files[0])
      let extension = e.target.files[0].name.split('.').pop()
      console.log(extension)
      if(extension !== "txt"){
        alert("File type should be .txt")
        setTextFile(null)  
        return
      }
      setTextFile(e.target.files[0])
    }
    const onZipFileChange = (e) => {
      console.log(e.target.files[0])
      let extension = e.target.files[0].name.split('.').pop()
      console.log(extension)
      if(extension !== "zip"){
        alert("File type should be zip")
        setZipFile(null) 
        return 
      }
      setZipFile(e.target.files[0])
    }

  if(loading) return <Loading />

  return (
    <div style={{
      display:"flex",
      justifyContent:"center",
      alignItems:"center",
      height:"80vh",
      // backgroundColor:"pink"
    }}>
      <Paper style={{
        minWidth: "50%",
        maxWidth: "100%",
        padding:"30px"
      }} elevation={5} >

        <div style={{ textAlign:"center" }}>
          <h2>
            Create Task 
          </h2>
        </div>

        <TextField 
          fullWidth
          style={{ marginTop:"10px" }} 
          value={taskName} 
          onChange={(e) => setTaskName(e.target.value)} 
          label="Task Name" 
          required
          id="Title" />
        <br></br><br></br>
        <TextField
          id="outlined-multiline-static"
          label="Task Description"
          fullWidth
          multiline
          rows={4}
          defaultValue=""
          required
          value={taskDescription} 
          onChange={(e) => setTaskDescription(e.target.value)}
        />

        <br></br><br></br>
        <label htmlFor="contained-button-file1">
          <Input 
            style={{ display:"none" }} 
            accept=".zip" 
            id="contained-button-file1" 
            type="file"
            onChange={onZipFileChange} 
            required
          />
          <Button variant="contained" component="span">
            Upload zip file
          </Button>
          {zipFile && zipFile.name ? <p>Uploaded zip file: {zipFile.name}</p> : "Zip file not uploaded"}
        </label>

        <br></br><br></br>

        <label htmlFor="contained-button-file2">
          <Input 
            style={{ display:"none" }} 
            accept=".txt" 
            id="contained-button-file2" 
            type="file"
            required
            onChange={onTextFileChange} 
          />
          <Button variant="contained" component="span">
            Upload text file
          </Button>
          {textFile && textFile.name ? <p>Uploaded text file: {textFile.name}</p> : "Text file not uploaded"}
        </label>

        <div style={{
          textAlign:"center"
        }}>
          <Button 
            variant="contained"
            onClick={submitForm}
            style={{ backgroundColor: "black", color:"white" }}
          >Submit</Button>
        </div>

      </Paper>
    </div>
  );
}


export default TaskForm;
