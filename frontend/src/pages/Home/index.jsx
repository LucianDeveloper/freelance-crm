import React from "react";
import drop from "../../media/img/drop.svg";
import edit from "../../media/img/edit.svg";
import bin from "../../media/img/bin.svg";
import telega from "../../media/img/telega.svg";


const Home = () => {
    return <div>
           <div className="clients_wrap">
            <div className="clients_top_block">
                <div className="new_client">
                    <h2>Клиентская база</h2>
                    <a href=""  className="btn_new_client">Добавить клиента</a>
                </div>
                <div className="surch">
                    <input className="surch_input" placeholder={"Поиск клиентов (по имени, email, телефону или данным мессенджеров)"} type="text" name="" id=""/>
                    <a href=""  className="btn_surch">Поиск</a>
                </div>
                <p className="clients_nbr"> 5 <span className="clients_nbr_text">записей о клиентах:</span></p>

            </div>
            <div className="wrap_wrap">
                <div className="clients_main">
                    <div className="table_test">
                        <tr className="sorting_wrap">
                            <input className="check" type="checkbox"/>
                            <td className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">ФИО/Название</p></td>
                            <td className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">Телефон</p></td>
                            <td className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">Telegram</p></td>
                            <td className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">Instagram</p></td>
                            <td className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">Покупки товаров</p></td>
                            <td className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">Заказы услуг</p></td>
                        </tr>

                        <tr className="client_table_item clients_table">
                            <input className="check"  type="checkbox"/>
                            <td className="client_inform_text"> Рыбочкин Михаил Романович <img  className="edit_img" src={edit} alt=""/></td>
                            <td className="client_inform_nbr"> +79803881508</td>
                            <td className="client_inform_text"> luciandeveloper</td>
                            <td className="client_inform_text"> lucian_dev2000</td>
                            <td className="client_inform_nbr_bold"> 1570 ₽</td>
                            <td className="client_inform_nbr_bold"> 0 ₽ </td>
                        </tr>
                        <tr className="client_table_item clients_table">
                            <input className="check"  type="checkbox"/>
                            <td className="client_inform_text"> Рыбочкин Михаил Романович <img  className="edit_img" src={edit} alt=""/></td>
                            <td className="client_inform_nbr"> +79803881508</td>
                            <td className="client_inform_text"> luciandeveloper</td>
                            <td className="client_inform_text"> lucian_dev2000</td>
                            <td className="client_inform_nbr_bold"> 1570 ₽</td>
                            <td className="client_inform_nbr_bold"> 0 ₽ </td>
                        </tr>
                        <tr className="client_table_item clients_table">
                            <input className="check"  type="checkbox"/>
                            <td className="client_inform_text"> Рыбочкин Михаил Романович <img  className="edit_img" src={edit} alt=""/></td>
                            <td className="client_inform_nbr"> +79803881508</td>
                            <td className="client_inform_text"> luciandeveloper</td>
                            <td className="client_inform_text"> lucian_dev2000</td>
                            <td className="client_inform_nbr_bold"> 1570 ₽</td>
                            <td className="client_inform_nbr_bold"> 0 ₽ </td>
                        </tr>
                        <tr className="client_table_item last clients_table"> {/*класс last для послднего элемента с классом client_table_item*/}
                            <input className="check"  type="checkbox"/>
                            <td className="client_inform_text"> Рыбочкин Михаил Романович <img  className="edit_img" src={edit} alt=""/></td>
                            <td className="client_inform_nbr"> +79803881508</td>
                            <td className="client_inform_text"> luciandeveloper</td>
                            <td className="client_inform_text"> lucian_dev2000</td>
                            <td className="client_inform_nbr_bold"> 1570 ₽</td>
                            <td className="client_inform_nbr_bold"> 0 ₽ </td>
                        </tr>
                    </div>

                </div>
                <div className="clients_side">
                    <div className="clients_side_card">
                        <p className="clients_side_card_title">Действия</p>
                        <p className="clients_side_card_subtitle">Операции</p>
                        <a href=""  className="clients_side_card_btn_blue"> <img  className="bin_img" src={bin} alt=""/>Удалить выбранных</a>
                        <a href=""  className="clients_side_card_btn_gray"> <img  className="bin_img" src={bin} alt=""/>Удалить всех найденных</a>
                        <p className="clients_side_card_subtitle">Рассылки</p>
                        <textarea  className="massage_input" placeholder={"Сообщение для клиентов"} type="text" name="" id=""/>
                        <a href=""  className="clients_side_card_btn_blue"> <img  className="telega_img" src={telega} alt=""/>Отправить выбранным</a>
                        <a href=""  className="clients_side_card_btn_gray"> <img  className="telega_img" src={telega} alt=""/>Отправить всем найденным</a>

                    </div>
                </div>
            </div>
        </div>
    </div>
}


export default Home