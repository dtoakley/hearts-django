import React, { Component } from 'react';

import { UncontrolledTooltip} from 'reactstrap';

import VoteList from '../Vote/List';
import ContentPopover from './Popover';
import './Index.css';
import { ACTION_TYPES, EMPTY_CONTENT_HTML_OPTIONS } from '../constants';

class Content extends Component {

    constructor(props) {
        super(props);
        this.state = {
            contentHtml: this.props.content.text,
            votedOn: this.props.votedOn,

        };
        this.updateVotedOn = this.updateVotedOn.bind(this);
        this.toggleVote = this.toggleVote.bind(this);
        this.handleContentChange = this.handleContentChange.bind(this);
        this.handleContentUpdate = this.handleContentUpdate.bind(this);
    };

    createMarkup() {
        return {__html: this.props.content.text};
    };

    toggleVote() {
        const voteData = {
            contentId: this.props.currentContentId,
            action: ACTION_TYPES.ADD_VOTE
        };

        if (this.props.votedOn === true) {
            voteData.action = ACTION_TYPES.REMOVE_VOTE;
        }

        this.props.sendWebsocketMessage(voteData);
    }

    updateVotedOn(status) {
        this.setState({
            votedOn: status
        });
    }

    handleContentChange(event) {
        this.setState({
            contentHtml: event.target.innerHTML
        });
    }

    handleContentUpdate() {
        const documentId = this.props.document.id;
        const contentId = this.props.content.id;

        let richText = this.state.contentHtml;

        if (richText.length < 1 || EMPTY_CONTENT_HTML_OPTIONS.indexOf(richText) > -1) {
            const contentData = {
                action: ACTION_TYPES.REMOVE_CONTENT,
                contentId: contentId
            };
            this.props.sendWebsocketMessage(contentData);
        } else {
            const contentData = {
                action: ACTION_TYPES.EDIT_CONTENT,
                documentId: documentId,
                contentId: contentId,
                text: richText.trim()
            };
            this.props.sendWebsocketMessage(contentData);
        }

    }

    render() {
        const content = this.props.content;
        const contentSelector = 'content-'.concat(content.id.toString());
        const showPopover = (this.props.currentContentId === content.id.toString());
        const tooltip = <UncontrolledTooltip placement="left" target={contentSelector}>
                {content.author} on {content.created_on}
            </UncontrolledTooltip>;
        const votedOn = this.props.votedOn;

        return (
            <div>
                <div className="ContentWrapper"
                     id={contentSelector}
                     onMouseEnter={this.props.handleContentMouseEnter}
                >
                    <div
                        className="Content"
                        onBlur={this.handleContentUpdate}
                        contentEditable={true}
                        dangerouslySetInnerHTML={this.createMarkup()}
                        onInput={this.handleContentChange}
                    >
                    </div>
                    <VoteList votes={this.props.votes}/>
                </div>
                {tooltip}
                <ContentPopover
                    showPopover={showPopover}
                    contentSelector={contentSelector}
                    toggleVote={this.toggleVote}
                    updateVotedOn={this.updateVotedOn}
                    votedOn={votedOn}
                />
            </div>

        );
    }
};

export default Content

