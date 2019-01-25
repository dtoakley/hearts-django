import React, { Component } from 'react';

import { FormGroup, Button, Form, FormFeedback, Input } from 'reactstrap';
import { Redirect } from 'react-router'

class DocumentForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            title: '',
            redirect: false,
            newDocumentId: null
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleFormSubmit = this.handleFormSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({title: event.target.value})
    }

    handleFormSubmit = () => {

        const documentData = {
            title: this.state.title
        };
        this.props.client.post(`api/documents`, documentData, (response) => {
            if (response.id) {
                this.setState({
                    redirect: true,
                    newDocumentId: response.id,
                })
            }
        });
    };

    render() {
        if (this.state.redirect) {
            return <Redirect to={`/doc/${this.state.newDocumentId}`} />
        } else {
            return (
                <div>
                    <h2>Create Document</h2>
                    <Form>
                        <FormGroup controlid="formBasicText">
                            <Input
                                type="text"
                                value={this.state.title}
                                placeholder="Enter title"
                                onChange={this.handleChange}
                            />
                            <FormFeedback />
                        </FormGroup>
                        <Button outline color="primary" onClick={this.handleFormSubmit}>Create document</Button>
                    </Form>
                </div>
            );
        }
    }
}

export default DocumentForm;