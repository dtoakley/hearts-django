import { Cookies } from 'react-cookie';
import { WebSocketBridge } from 'django-channels';

class Client {

    constructor() {
        this.cookies = new Cookies();
    }

    get(endpoint, callback) {
        const headers = this.buildHeaders();

        return fetch(endpoint, {
            credentials: "same-origin",
            headers: headers
        }).then((response) => (response.json()))
            .then((callback));
    }

    post(endpoint, data, callback) {
        return this.request(endpoint, data, "POST", callback);
    }

    put(endpoint, data, callback) {
        return this.request(endpoint, data, "PUT", callback);
    }

    delete(endpoint, data, callback) {
        return this.request(endpoint, data, "DELETE", callback);
    }

    request(endpoint, data, method, callback) {
        const formData = new FormData();
        const headers = this.buildHeaders();

        for (let property in data) {
            if (data.hasOwnProperty(property)) {
                formData.append(property, data[property]);
            }
        }

        return fetch(endpoint, {
            method: method,
            credentials: "same-origin",
            headers: headers,
            body: formData,
        }).then((response) => (response.json()))
            .then((callback));
    }

    buildHeaders() {
        const headers = new Headers();
        const csrfToken = this.cookies.get('csrftoken');
        if (csrfToken) {
            headers.append("Authorization", "Token " + csrfToken);
        }
        return headers;
    }

    connectWebSocket() {
        const webSocketScheme = window.location.protocol === "https:" ? "wss" : "ws";
        return new WebSocket(webSocketScheme + '://' + window.location.hostname + ':8000' + window.location.pathname);
    }

}

export default Client;
