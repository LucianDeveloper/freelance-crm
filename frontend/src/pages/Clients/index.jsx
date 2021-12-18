import React, {useEffect, useState} from "react";
import drop from "../../media/img/drop.svg";
import bin from "../../media/img/bin.svg";
import edit from "../../media/img/edit.svg";
import telega from "../../media/img/telega.svg";
import Modal from "../../components/Modal";
import Record from "./Record";
import api from "../../utils/api";


const Clients = () => {
    const [clientId, setClientId] = useState(null);
    const [items, setItems] = useState(null)

    useEffect(() => {
        api('/clients/').then((result) => {
            setItems(result)
        })
    }, [])

    return <div>
        <Modal title={''}
               content={
                   <div className="modal-content">
                       <p className="modal_title">Информация о клиенте</p>
                       <p className="modal_subtitle">ФИО</p>
                       <input className="modal_input" value={"Рыбочкин Михаил Романович"} type="text" name="" id=""/>
                       <p className="modal_subtitle">Номер телефона</p>
                       <input className="modal_input_tel" value={"+79803881508"} type="text" name="" id=""/>
                       <p className="modal_subtitle">Telegram</p>
                       <input className="modal_input" value={"luciandeveloper"} type="text" name="" id=""/>
                       <p className="modal_subtitle">Instagram</p>
                       <input className="modal_input" value={"lucian_dev2000"} type="text" name="" id=""/>
                       <p className="modal_subtitle_center">Примечания</p>
                       <textarea  className="modal_massage_input" value={"Повседневная практика показывает, что укрепление и развитие структуры обеспечивает широкому кругу..."} type="text" name="" id=""/>
                       <a href=""  className="btn_save">Сохранить</a>
                   </div>
               }
               footer={''}
               visible={clientId !== null}
               onClose={() => setClientId(null)}
        />
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
                        {
                            (items !== null) && items.map((item, index, array) => {
                                return <Record item={item}
                                               setClientId={setClientId}
                                               index={index}
                                               maxIndex={array.length - 1}
                                />
                            })
                        }
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


export default Clients