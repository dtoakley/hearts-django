import React from 'react';
import { NavLink } from 'reactstrap';
import { withRouter } from 'react-router-dom';


const LoginButton = withRouter(({ auth, history }) => (
    auth.loggedIn() ? (
        <NavLink href="/logout" onClick={() => {
            auth.logout(() => history.push('/'))
        }}>Logout</NavLink>
    ) : (
        <NavLink href="/login">Login</NavLink>
    )
));

export default LoginButton;