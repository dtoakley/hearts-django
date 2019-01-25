import { Cookies } from 'react-cookie';

import Client from './Client';


class Auth {

    constructor()  {
        this.cookies = new Cookies();
    }

    login(username, pass, callback) {
        const csrfToken = this.cookies.get('csrftoken');
        if (csrfToken) {
            callback({token: csrfToken});
            return
        }
        this.getToken(username, pass, (res) => {
            if (res.authenticated) {
                callback(res);
            }
        })
    }

    logout(callback) {
        this.cookies.remove('csrftoken');
        callback();
    }

    loggedIn() {
        return !!this.cookies.get('csrftoken');
    }

    getToken(username, password, callback) {
        const client = new Client();
        const userData = {
            username: username,
            password: password
        };

        client.post(`/api/obtain-auth-token`, userData, (response) => {
            callback({
                authenticated: true,
                token: response.token,
            });
        });
    }
};

export default Auth;