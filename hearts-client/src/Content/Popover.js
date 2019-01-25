import React from 'react';
import {Popover, PopoverHeader} from 'reactstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeart } from '@fortawesome/free-solid-svg-icons';

import './Popover.css';

const ContentPopover = ({showPopover, contentSelector, toggleVote, updateVotedOn, votedOn}) => {
    return (
        <Popover isOpen={showPopover} target={contentSelector}>
            <PopoverHeader>Actions</PopoverHeader>
            <div className="popover-actions">
                <p className={"text-muted " + (votedOn ? 'voted-on' : '')} onClick={() =>{toggleVote(); updateVotedOn(true);}}>
                    <FontAwesomeIcon icon={faHeart} size="lg" />
                    Heart{votedOn ? 'ed': ''}
                </p>
            </div>

        </Popover>
    );
};

export default ContentPopover;
