import React, {useState} from 'react';
import {useAuth} from "../../utils/authContext";


const Footer = () => {
    return <div className="footer">
        <div className="wrap">
            <div className="footer_link_block">
                <a className="footer_link_p" href="">Лицензионное соглашение</a>
                <a className="footer_link" href="">Политика конфиденциальности</a>
            </div>
            <div>
                <p className="footer_text">© Название проекта, 2021 г.</p>
            </div>
        </div>
    </div>
}


export default Footer
