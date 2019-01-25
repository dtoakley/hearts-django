import React from 'react';

import { FormGroup, Label, Form, FormFeedback, Input } from 'reactstrap';

const ArchiveSearch = ({searchTerm, handleArchiveSearch}) => {
    return (
        <Form>
            <FormGroup controlid="formBasicText">
                <Label>Search the document archive</Label>
                <Input
                    type="text"
                    value={searchTerm}
                    placeholder="Enter text"
                    onChange={handleArchiveSearch}
                />
                <FormFeedback />
            </FormGroup>
        </Form>
    );
};

export default ArchiveSearch;


