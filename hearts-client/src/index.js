import React from 'react';
import ReactDOM from 'react-dom';

import registerServiceWorker from './registerServiceWorker';
import { BrowserRouter, Route,  Switch, Redirect } from 'react-router-dom';
import Auth from './Utils/Auth';
import HeartsNav from './Nav/Index';

import Archive from './Archive/Index';
import Document from './Document/Index';
import Login from './Login';
import App from './App';

import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';

const auth = new Auth();

const PrivateRoute = ({ component: Component, ...rest }) => (
    <Route {...rest} render={props => (
        auth.loggedIn() ? (
            <Component {...props}/>
        ) : (
            <Redirect to={{
                pathname: '/login',
                state: { from: props.location }
            }}/>
        )
    )}/>
);


ReactDOM.render(
    <BrowserRouter>
        <div>
        <HeartsNav auth={auth} />
            <Switch>
                <Route exact path='/login' component={Login}/>
                <PrivateRoute exact path='/' component={App}/>
                <PrivateRoute exact path='/archive' component={Archive} />
                <PrivateRoute path='/doc/:documentId' component={Document} />
            </Switch>
        </div>
    </BrowserRouter>,
    document.getElementById('root'));
registerServiceWorker();
