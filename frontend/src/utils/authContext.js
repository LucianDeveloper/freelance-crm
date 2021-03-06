import React, {useContext, createContext, useState, useEffect} from "react";
import ky from "ky";
import {host} from "./rawApi";
import historyRef from "./history";
import {NotificationManager} from "react-notifications";
import api from "./api";


const authContext = createContext(3);

function ProvideAuth({ children }) {
    const auth = useProvideAuth();
    return (
        <authContext.Provider value={auth}>
            {children}
        </authContext.Provider>
    );
}

function useAuth() {
    return useContext(authContext);
}

function useProvideAuth() {
    const [user, setUser] = useState(null);

    useEffect(() => {
        getCurrent()
    }, [])

    const getCurrent = () => {
        api('/users/me').then((result) => {
            setUser(result)
        }).catch((_) => {
            // historyRef.navigate('/login')
        });
    }

    const signIn = (username, password) => {
        ky.post(`${host}/auth/jwt/login`, {
            body: new URLSearchParams(`username=${username}&password=${password}`), timeout: 2 * 60 * 1000,
            credentials: 'include',
        }).then((response) => {
            if (response.ok) {
                api('/users/me').then((result) => {
                    setUser(result)
                }).then(() => {
                    historyRef.navigate('/');
                }).catch((_) => {
                    // historyRef.navigate('/login')
                });
            } else if (response.status === 401){
                NotificationManager.error(
                    'При аворизации произошла ошибка! Пожалуйста, проверьте логин и пароль',
                    '', 5000
                )
            } else {
                NotificationManager.error(
                    'Произошла неизвестная ошибка. Попробуйте позже или обратитесь к разработчику',
                    '', 5000
                )
            }
        }).catch(() => NotificationManager.error(
            'Произошла неизвестная ошибка. Попробуйте позже или обратитесь к разработчику',
            '', 5000
        ))
    };

    const signOut = () => {
        setUser(null);
    };

    return {
        user,
        getCurrent,
        signIn,
        signOut
    };
}


export {useAuth, useProvideAuth, ProvideAuth}
