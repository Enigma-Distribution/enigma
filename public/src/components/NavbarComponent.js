import * as React from 'react';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import { useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

function NavbarComponent() {
    let history = useHistory();

    const userInfo = useSelector((state) => state.user);
    const { user } = userInfo 
    const dispatch = useDispatch()

    const sections = [
        {
            title: "Login",
            url: "/login",
            show: user ? false : true,
            position: "right"
        },
        {
            title: "register",
            url: "/register",
            show: user ? false : true,
            position: "right"
        },
        {
            title: "Home",
            url: "/main",
            show: user ? true : false,
            position: "left"
        },
        {
            title: "Create Task",
            url: "/TaskForm",
            show: user ? true : false,
            position: "left"
        },
        {
            title: "About Us",
            url: "/about",
            show: true,
            position: "left"
        },
        // {
        //     title: "Contribute",
        //     url: "/contribute",
        //     show: true
        //     position: "left"
        // },
        {
            title: "Logout",
            url: "/logout",
            show: user ? true : false,
            position: "right"
        }
        
    ]

    return (
        <React.Fragment>
            <Toolbar sx={{ borderBottom: 1, borderColor: 'divider' }}>
                {/* <Button size="small">Subscribe</Button> */}
                <Typography
                component="h2"
                variant="h5"
                color="inherit"
                align="center"
                noWrap
                sx={{ flex: 1 }}
                >
                Enigma
                </Typography>
                {/* <Button variant="outlined" size="small">
                Sign up
                </Button> */}
            </Toolbar>
            <Toolbar
                component="nav"
                variant="dense"
                sx={{ justifyContent: 'space-between', overflowX: 'auto' }}
            >
                {/* left */}
                <div>
                    {sections.map((section) => (
                        
                    section.show && section.position === "left" && <Link
                        color="inherit"
                        noWrap
                        key={section.title}
                        variant="body2"
                        href={section.url}
                        sx={{ p: 1, flexShrink: 0 }}
                    >
                        {section.title}
                    </Link>

                    ))}
                </div>

                {/* right */}
                <div>
                    {sections.map((section) => (
                        
                    section.show && section.position === "right" && <Link
                        color="inherit"
                        noWrap
                        key={section.title}
                        variant="body2"
                        href={section.url}
                        sx={{ p: 1, flexShrink: 0 }}
                        onClick={() => {
                            if(section.title === "Logout"){
                                dispatch({type: "SET_USER", payload: null})
                                localStorage.removeItem("USER")
                                // history.push("/login")
                            }
                        }}
                    >
                        {section.title}
                    </Link>

                    ))}
                </div>

            </Toolbar>
            </React.Fragment>
    )


    return (
        <div style={{
            height: "60px",
            width:"100%",
            backgroundColor: "cyan"
        }}>
            Navbar {"       -      "}
            <a href="/login">login</a> {"       -      "}
            <a href="/register">register</a> {"       -      "}
            <a href="/main">main</a> {"       -      "}
            <a href="/SingleTask">SingleTask</a> {"       -      "}
            <a href="/TaskForm">TaskForm</a> 
        </div>
    );
}

export default NavbarComponent;
