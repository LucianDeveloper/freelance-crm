import React from "react";
import './header.scss';
import logo from "../../media/img/logo 2.svg"
import client from "../../media/img/clients.svg"
import lock from "../../media/img/lock.svg"
import money from "../../media/img/money.svg"
import smm from "../../media/img/smm.svg"
import product from "../../media/img/products.svg"
import timetable from "../../media/img/timetable.svg"
import exit from "../../media/img/exit.svg"
import main from "../../media/img/main.svg"


const Header = () => {

    return <div className='header'>
        <div className="header_wrap">
            <div><img  className="header_img" src={logo} alt=""/></div>
            <div>
                <nav className="menu">
                     <div className="menu_link"><a className="link_menu" href="">
                        <div className="menu_item">
                            <img  className="menu_img" src={main} alt=""/>
                            <p className="menu_title">Главная</p>
                        </div>
                    </a></div>
                    <div className="menu_link"><a className="link_menu" href="">
                        <div className="menu_item">
                            <img  className="menu_img" src={timetable} alt=""/>
                            <p className="menu_title">Расписание</p>
                        </div>
                    </a></div>
                    <div className="menu_link"><a className="link_menu" href="">
                        <div className="menu_item">
                            <img  className="menu_img" src={client} alt=""/>
                            <p className="menu_title">Клиенты</p>
                        </div>
                    </a></div>
                    <div className="menu_link"><a className="link_menu" href="">
                        <div className="menu_item">
                            <img  className="menu_img" src={product} alt=""/>
                            <p className="menu_title">Товары</p>
                        </div>
                    </a></div>
                    <div className="menu_link"><a className="link_menu" href="">
                        <div className="menu_item">
                            <img  className="menu_img" src={lock} alt=""/>
                            <p className="menu_title">Услуги</p>
                        </div>
                    </a></div>
                    <div className="menu_link"><a className="link_menu" href="">
                        <div className="menu_item">
                            <img  className="menu_img" src={money} alt=""/>
                            <p className="menu_title">Кошелек</p>
                        </div>
                    </a></div>
                    <div className="menu_link"><a className="link_menu" href="">
                        <div className="menu_item">
                            <img  className="menu_img" src={smm} alt=""/>
                            <p className="menu_title">Продвижение</p>
                        </div>
                    </a></div>
                </nav>
            </div>
            <div className="header_person">
                <div className="person_info">
                    <p className="person_name">Кулешова Е. А.</p>
                    <p className="person_inn">7841501689</p>
                </div>
                <a href=""><img  className="exit_img" src={exit} alt=""/></a>
            </div>
        </div>
    </div>
}



export default Header