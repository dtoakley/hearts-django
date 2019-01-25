import React, { Component } from 'react';

import { Link } from 'react-router-dom';
import Client from '../Utils/Client';
import { Container, Col, Row } from 'reactstrap';
import ArchiveSearch from './Search';

class Archive extends Component {

    constructor(props) {
        super(props);
        this.state = {
            searchTerm: '',
            documents: [],
            searchResults: []
        };
        this.handleArchiveSearch = this.handleArchiveSearch.bind(this);
    }

    componentWillMount() {
        const client = new Client();

        client.get(`/api/documents`, (response) => {
            this.setState({
                documents: response,
                searchResults: response
            });
        });
    }

    handleArchiveSearch(event) {
        const searchTerm = event.target.value;
        let searchResults = [];

        this.state.documents.forEach((document) => {
           if (document.title.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1) {
               searchResults.push(document);
           }
        });
        this.setState({
            searchTerm: event.target.value,
            documents: this.state.documents,
            searchResults: searchResults,
        });

    }

    render() {
        const documents = this.state.searchResults;
        return (
            <Container>
                <Row>
                    <Col md={6}>
                        <h2>Document Archive</h2>
                        <ArchiveSearch searchTerm={this.state.searchTerm} handleArchiveSearch={this.handleArchiveSearch}/>
                        <ul>
                            {documents.map(document => (
                                <li key={document.id}>
                                    <Link to={`/doc/${document.id}`}>{document.title}</Link>
                                </li>
                            ))}
                        </ul>
                    </Col>
                </Row>
            </Container>
        );
    }
}

export default Archive;
