import React, { useState } from 'react';
import { useSelector } from 'react-redux';
import { Redirect, Route } from 'react-router-dom';
import Loading from './Loading';

export default function PrivateRoute(props) {
    const Component = props.component
    // const [loading, setLoading] = useState(true)

    const userInfo = useSelector((state) => state.user);
    const { user } = userInfo 

    // if(loading) {
    //     return <Loading />
    // }
    
    
    return (
        <Route 
            user={user}
            render = {(props) =>
            user ? (
                <>
                    <Component user={user} {...props}></Component>
                </>
            ) : (
                <Redirect to="/login" />
            )
        }
        ></Route>
    );
}









// if(props.user && !window.location.href.includes("/login")){
        //     console.log("Not on login page")
        //     const lastTokenUpdatedOn = parseInt(localStorage.getItem("tokenTime")) // minutes => 32
        //     const currentTime = new Date().getMinutes()
        //     const timeLimit = 10
        //     console.log(lastTokenUpdatedOn, currentTime, (lastTokenUpdatedOn + timeLimit) - currentTime)
        //     if(!lastTokenUpdatedOn || (lastTokenUpdatedOn + timeLimit) - currentTime < 0){
        //         props.setUser(null)
        //     }
        //     else{
        //         // user is already set to go. His token is not expired 
        //     }
        // }
        // setLoading(false)