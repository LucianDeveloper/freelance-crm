import React from 'react';
import {useNavigate} from 'react-router-dom';
import historyRef from '../../utils/history';

const HistoryThief = () => {
	const navigate = useNavigate();

	React.useEffect(
		() => {
			historyRef.navigate = navigate;
		},
		[navigate]
	);

	return null;
};

export default HistoryThief;
