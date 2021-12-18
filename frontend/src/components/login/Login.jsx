import React, {useState} from 'react';
import {useAuth} from "../../utils/authContext";
import Footer from "../footer";
import logo_black from "../../media/img/logo_black.svg"


const Login = () => {
	const [username, setUsername] = useState(null);
	const [password, setPassword] = useState(null);

	let auth = useAuth();

	const onSubmit = () => auth.signIn(username, password);

	return (

			<div className="login_wrap">
				<form className="log_in_form" onSubmit={onSubmit}>
					<div className="name_field">
						<div><img  className="logo_img" src={logo_black} alt=""/></div>
						<p className="name_field_text">cистема автоматизированного менеджмента для самозанятых</p>

					</div>
					<div className="log_in_fields">
						<h3>Вход</h3>
						<input className="input_mail" placeholder={"Электронная почта"} type="text" name="" id=""/>
						<input className="input_pass" placeholder={"Пароль"} type="password" name="" id=""/>
					</div>
					<a href="/" className="btn_enter" type="submit">Отправить</a>
					<div className="centr">
						<a href={"/"} className="registration_link">Регистрация</a>
					</div>
				</form>
			</div>
	);
};

export default Login;
