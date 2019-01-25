import React from 'react';

import {UncontrolledTooltip} from 'reactstrap';
import FontAwesomeIcon from '@fortawesome/react-fontawesome';
import faHeart from '@fortawesome/fontawesome-free-solid/faHeart';


const Vote = ({vote}) => {

    const voteSelector = 'vote-'.concat(vote.id);
    return (
        <span>
            <UncontrolledTooltip placement="top" target={voteSelector}>
                {vote.author}
            </UncontrolledTooltip>
            <FontAwesomeIcon id={voteSelector} icon={faHeart} size="lg" />
        </span>
    )
};

export default Vote;