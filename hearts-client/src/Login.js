import React, { Component } from 'react';
import { Cookies } from 'react-cookie';

import Auth from './Utils/Auth';
import { Container, Col, Row, FormGroup, Input, Button, Form, FormFeedback } from 'reactstrap';
import { Redirect } from 'react-router-dom';

class Login extends Component {

    constructor(props) {
        super(props);
        this.state = {
            redirectToReferrer: false,
            username: '',
            password: ''
        };
        this.handleChange = this.handleChange.bind(this);
        this.handLoginClick = this.handLoginClick.bind(this);
        this.cookies = new Cookies();
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    handLoginClick() {
        const auth = new Auth();
        auth.login(this.state.username, this.state.password, (response) => {
            if (response.token) {
                this.cookies.set('csrftoken', response.token);
                this.setState({ redirectToReferrer: true });
            }
        });
    }

    render() {
        const { from } = this.props.location.state || { from: { pathname: '/' } };

        if (this.state.redirectToReferrer) {
            return (
                <Redirect to={from}/>
            )
        }
        return (
            <Container>
                <Row>
                    <Col md={4} className="loginWrapper">
                        <h2>Login</h2>
                        <Form onChange={this.handleChange}>
                            <FormGroup controlid="formBasicText">
                                <Input
                                    type="text"
                                    placeholder="Username"
                                    name="username"
                                />
                                <FormFeedback />
                            </FormGroup>
                            <FormGroup controlid="formBasicText">
                                <Input
                                    type="password"
                                    placeholder="Password"
                                    name="password"
                                />
                                <FormFeedback />
                            </FormGroup>
                            <Button outline color="primary" onClick={this.handLoginClick}>Login</Button>
                        </Form>
                    </Col>
                </Row>
            </Container>
        );
    }
}

export default Login;