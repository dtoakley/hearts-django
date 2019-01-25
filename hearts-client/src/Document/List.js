import React, { Component } from 'react';

import { Link } from 'react-router-dom';

class DocumentList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            documents: []
        };
    }

    componentWillMount() {
        this.props.client.get(`api/documents`, (response) => {
            this.setState({documents: response});
        });
    }

    render() {
        const documents = this.state.documents;
        return (
            <div>
                <h2>Recent Documents</h2>
                <ul>
                    {documents.map(document => (
                        <li key={document.id}>
                            <Link to={`doc/${document.id}`}>{document.title}</Link>
                        </li>
                    ))}
                </ul>
            </div>
        );
    }
}

export default DocumentList;