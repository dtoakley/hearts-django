import React, { Component } from 'react';
import { Container, Col, Row} from 'reactstrap';
import Client from '../Utils/Client';
import ContentForm from '../Content/Form';
import ContentList from '../Content/List';
import './Index.css';

class Document extends Component {

    constructor(props) {
        super(props);
        this.state = {
            user: {},
            document: {},
            contents: [],
            currentContentId: null,
            showPopover: false,
        };
        this.handleContentMouseEnter = this.handleContentMouseEnter.bind(this);
        this.client = new Client();
        this.websocket = this.client.connectWebSocket();
        this.onWebsocketMessage = this.onWebsocketMessage.bind(this);
        this.websocket.onmessage = this.onWebsocketMessage;
        this.sendWebsocketMessage = this.sendWebsocketMessage.bind(this);
    }

    componentDidMount() {

        const documentId = parseInt(this.props.match.params.documentId, 10);

        this.client.get(`/api/documents/${documentId}`, (response) => {
            this.setState({document: response});
        });

        this.client.get(`/api/documents/${documentId}/contents`, (response) => {
            this.setState({contents: response});
        });

        this.client.get(`/api/users/i`, (response) => {
            this.setState({user: response})
        });
    }

    handleContentMouseEnter(event) {
        const content = (event.target.className === 'Content')
            ? event.target.parentElement : event.target;
        const contentId = content.id.replace('content-', '');

        this.setState({
            currentContentId: contentId,
            showPopover: true,
        });
    }

    sendWebsocketMessage(message) {
        message.user = this.state.user;
        this.websocket.send(
            JSON.stringify(message)
        );
    }

    onWebsocketMessage(message) {
        let messageData = JSON.parse(message.data).text;
        let contents = this.state.contents;
        let newContent = true;

        if (messageData.contentDeletedId) {
            newContent = false;
            for(let i = 0; i < contents.length; i++) {
                if(contents[i].id === parseInt(messageData.contentDeletedId, 10)) {
                    contents.splice(i, 1);
                    break;
                }
            }
        }

        contents.forEach(function(content) {
            if (content.id === messageData.id) {
                let index = contents.indexOf(content);
                contents[index] = messageData;
                newContent = false;
            }
        });

        if (newContent) {
            contents.push(messageData);
        }

        this.setState({
            document: this.state.document,
            contents: contents,
            currentContentId: this.state.currentContentId
        });
    }

    render() {
        const document = this.state.document;
        return (
            <Container fluid={true} className="DocumentContainerFluid">
                <Container className="DocumentContainer">
                    <Row>
                        <Col>
                            <div className="DocumentHead">
                                <h1>{document.title}</h1>
                            </div>
                            <ContentList
                                user={this.state.user}
                                document={document}
                                sendWebsocketMessage={this.sendWebsocketMessage}
                                contents={this.state.contents}
                                handleContentMouseEnter={this.handleContentMouseEnter}
                                currentContentId={this.state.currentContentId}
                                showPopover={this.state.showPopover}
                                handleAddVote={this.toggleVote}
                                handleRemoveVote={this.handleRemoveVote}
                            />
                            <ContentForm
                                client={this.client} documentId={document.id}
                                sendWebsocketMessage={this.sendWebsocketMessage}
                            />
                        </Col>
                    </Row>
                </Container>
            </Container>
        )
    }

};

export default Document;
