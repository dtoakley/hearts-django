import React, { Component } from 'react';
import {Container, Row, Col} from 'reactstrap';
import DocumentForm from './Document/Form';
import DocumentList from './Document/List';

import Client from './Utils/Client';


class App extends Component {

    constructor(props) {
        super(props);
        this.user = {};
    }

    componentDidMount() {
        const client = new Client();

        client.get(`/api/users/i`, (response) => {
            this.setState({user: response})
        });
    }

    render() {
        const client = new Client();
        return (
            <Container>
                <Row>
                    <Col md={6}>
                        <DocumentForm client={client} />
                    </Col>
                    <Col md={6}>
                        <DocumentList client={client} />
                    </Col>
                </Row>
            </Container>
        );
    }
}



export default App;
