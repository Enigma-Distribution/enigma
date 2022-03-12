import './App.css';
import * as React from 'react';
import ReactDOM from 'react-dom';
import Button from '@mui/material/Button';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Login from './screens/Login';
import Register from './screens/Register'
import Main from './screens/Main'
import TaskForm from './screens/TaskForm'
import SingleTask from './screens/SingleTask'
import RoutesTemporary from './screens/RoutesTemporary';
import NavbarComponent from './components/NavbarComponent';
import PrivateRoute from './components/PrivateRoute';
import { useDispatch, useSelector } from 'react-redux';

function App() {
  
  const dispatch = useDispatch()
  // const userInfo = useSelector((state) => state.user);
  // const { user } = userInfo 

  return (
    <div>
      {/* <button onClick={() => dispatch({type: "SET_USER", payload: { username: "dummyun" }})}></button> */}
     <NavbarComponent />
     {/* {JSON.stringify(user)} */}
      <Router>
        <div>
          <Switch>
            <Route exact path="/login">
              <Login  />
            </Route>
            <Route exact path="/register">
              <Register />
            </Route>
            <PrivateRoute
              path="/main"
              component={Main}
              
            ></PrivateRoute>
            {/* <Route exact path="/main">
              <Main />
            </Route> */}
            <PrivateRoute
              path="/task/:id"
              component={SingleTask}
            ></PrivateRoute>
            {/* <Route exact path="/task/:id">
              <SingleTask />
            </Route> */}
            <PrivateRoute
              path="/TaskForm"
              component={TaskForm}
            ></PrivateRoute>
            {/* <Route exact path="/TaskForm">
              <TaskForm />
            </Route> */}
            
            <PrivateRoute
              path="/"
              component={Main}
              
            ></PrivateRoute>
            
          </Switch>
        </div>

      </Router>

    </div>
  );
}

export default App;
