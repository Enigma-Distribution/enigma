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

import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function createData(
  word: string,
  count: number,
) {
  return { word, count };
}

const rows = [
  createData('Frozen yoghurt', 159),
];

export default function ResultTable() {

    // cid of result file
    const cid = window.location.href.split("/resulttable/")[1]
    const [data,setData] = React.useState("")

    React.useEffect(() => {
        fetch('https://ipfs.infura.io/ipfs/'+cid)
        .then(response => response.json())
        .then(json => {
            // setData(json)
            // json = JSON.parse(json);
            // console.log(json)
            // console.log(typeof(json))
            let z = []
            Object.keys(json).forEach(key => {
                let value = json[key];
                console.log(key, value);
                z.push([key,value])
            });

            setData(z)
              
        })
    },[])

    // return <h1>Hey</h1>
    // let z = <></>
    

  return (

    <Container>
        <div style={{ padding:"30px", textAlign:"center", width:"100%" }}>
        Result File: {"  "}  
        <a href={`https://ipfs.infura.io/ipfs/${cid}`}>{`https://ipfs.infura.io/ipfs/${cid}`}</a>
      
        </div>
        <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} size="small" aria-label="a dense table">
        <TableHead>
          <TableRow>
            <TableCell>Word</TableCell>
            <TableCell align="right">Count</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>

        
            

          {data && data.map((d) => {
              let key = d[0]
              let value = d[1]
              return (
                <TableRow
                  key={key}
                  sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                >
                  <TableCell component="th" scope="row">
                    {key}
                  </TableCell>
                  <TableCell align="right">{value}</TableCell>
                </TableRow>
              )
            } 
          
          )}
        </TableBody>
      </Table>
    </TableContainer>
    </Container>
  );
}