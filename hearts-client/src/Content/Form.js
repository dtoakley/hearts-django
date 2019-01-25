import React, { Component } from 'react';

import { Button } from 'reactstrap';

import { ACTION_TYPES } from '../constants';
import './Form.css';

class ContentForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            text: ''
        };
        this.handleContentSubmit = this.handleContentSubmit.bind(this);
    }

    handleContentSubmit = (event) => {
        const documentId = this.props.documentId;
        const sendWebsocketMessage = this.props.sendWebsocketMessage;
        const contentHtml = decodeURIComponent(encodeURIComponent(event.target.innerHTML));

        if (contentHtml.length > 0 && contentHtml !== '<br>') {
            const contentData = {
                action: ACTION_TYPES.ADD_CONTENT,
                documentId: documentId,
                text: contentHtml,
                contentId: null
            };

            sendWebsocketMessage(contentData);
            event.target.innerHTML = '';
        }
    };

    createMarkup() {
        return {__html: this.state.text};
    }

    render() {
        return (
            <div className="content-form-wrapper">
                <h4>Add your idea:</h4>
                <div
                    id="ContentForm"
                    disabled={false}
                    onBlur={this.handleContentSubmit}
                    className="ContentFrom"
                    contentEditable={true}
                    onFocus={this.props.handleContentFormFocus}
                    dangerouslySetInnerHTML={this.createMarkup()}
                />
                <Button outline color="primary" className="content-form-button">Add idea</Button>
            </div>
        );
    }
}

export default ContentForm;