import ky from 'ky';
import historyRef from './history';
import {NotificationManager} from "react-notifications";

const host = process.env.REACT_APP_URL || 'http://127.0.0.1:8000/api'

const rawApi = (url, {headers, ...options} = {}, withHost=false) => {
	return ky(
		`${(withHost) ? "" : host}${url}`,
		{
			timeout: 2 * 60 * 1000,
			headers: {
				...headers
			},
			credentials: 'include',
			hooks: {
				afterResponse: [
					(request, options, response) => {
						if (response.status === 401) {
							historyRef.navigate('/login');
						} else if (response.status >= 300) {
							historyRef.navigate('/');
							NotificationManager.error(`Статус ошибка: ${response.status}`, 'Ошибка при запросе', 5000)
						}
					}
				]
			},
			...options
		}
	);
}

export default rawApi;
export {host}
