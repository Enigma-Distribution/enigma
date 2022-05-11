import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Container from '@mui/material/Container';
import { BarChart } from '../charts/BarChart';
import { LineChart } from '../charts/LineChart';
import { PieChart } from '../charts/PieChat';

export default function UserProfile() {

  const id = window.location.href.split("/profile/")[1]

  // return <Linecharts />

  return (
    
    <Container style={{ }}>

      <div style={{ display:"flex", justifyContent:"center" }}>
        <div style={{ }}>
          <Avatar
            alt="Remy Sharp"
            src="https://mui.com/static/images/avatar/1.jpg"
            sx={{ width: 150, height: 150 }}
            style={{margin:"auto"}}
          />
          <p style={{ textAlign:"center" }}>Remy Sharp - {id}</p>
        </div>
      </div>

      <div>
        <br></br><br></br><br></br>
        <BarChart />
        <br></br><br></br><br></br>
        <LineChart />
        <br></br><br></br><br></br>
        <div style={{ display:"flex", justifyContent:"center" }}>
          <div style={{ width:"50%" }}>
            <PieChart />
          </div>
        </div>
        <br></br><br></br><br></br>
      </div>

    </Container>

  );
}