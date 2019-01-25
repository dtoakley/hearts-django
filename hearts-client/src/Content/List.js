import React from 'react';

import Content from './Index';
import './List.css';

const ContentList = ({user, document, sendWebsocketMessage, showPopover, contents, handleContentMouseEnter,
                         handleContentUpdate, currentContentId, handleAddVote, handleRemoveVote}) => {

    return (
        <div className="ContentList">
                {contents.map((content) => {
                    let votedOn = false;

                    content.votes.find((element)=> {
                        if (element.author === user.username) {
                            votedOn = true;
                        }
                    });

                    return (
                        <Content
                            key={content.id}
                            user={user}
                            content={content}
                            votes={content.votes}
                            sendWebsocketMessage={sendWebsocketMessage}
                            document={document}
                            handleContentMouseEnter={handleContentMouseEnter}
                            handleContentUpdate={handleContentUpdate}
                            currentContentId={currentContentId}
                            showPopover={showPopover}
                            handleAddVote={handleAddVote}
                            handleRemoveVote={handleRemoveVote}
                            votedOn={votedOn}
                        />
                    )
                })}
        </div>
    )
};

export default ContentList;