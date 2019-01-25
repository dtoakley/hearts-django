import React from 'react';

import Vote from './Index';

import './List.css';

const VoteList = ({votes}) => {

    return (
        <span className="VoteList">
            {votes.map((vote) => {
                return (
                    <Vote
                        key={vote.id}
                        vote={vote}>
                    </Vote>
                )
            })}
        </span>
    );
};

export default VoteList;