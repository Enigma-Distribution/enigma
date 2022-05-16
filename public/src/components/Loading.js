import { CircularProgress } from '@mui/material';
import { flexbox } from '@mui/system';
import React from 'react';

function Loading(props) {
    return (
        <div style={{ display: "flex", flexDirection:"column", height:"80vh", width:"100%", flex: 1, alignItems:"center", justifyContent:"center" }} >
            <CircularProgress color="secondary" />
            {/* <p>Please wait while we break you task into steps</p> */}
        </div>
    );
}

export default Loading;