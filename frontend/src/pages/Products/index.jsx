import React, {useState} from "react";
import drop from "../../media/img/drop.svg";
import bin from "../../media/img/bin.svg";
import edit from "../../media/img/edit.svg";
import telega from "../../media/img/telega.svg";
import Modal from "../../components/Modal";


const Products = () => {
    const [clientId, setClientId] = useState(null);

    return <div>


        <Modal title={''}
                content={
                   <div className="modal-content">
                       <p className="modal_title">Информация о товаре</p>
                       <p className="modal_subtitle">Наименование</p>
                       <input className="modal_input" value={"Шапка вязаная “Балаклава"} type="text" name="" id=""/>
                       <p className="modal_subtitle">Количество в наличии</p>
                       <input className="modal_input_tel" value={"15"} type="text" name="" id=""/>
                       <p className="modal_subtitle">Цена за единицу ₽</p>
                       <input className="modal_input_tel" value={"1570"} type="text" name="" id=""/>
                       <p className="modal_subtitle">Категория</p>
                       <input className="modal_input" value={"handmade"} type="text" name="" id=""/>
                       <p className="modal_subtitle">Количество заказов</p>
                           <input className="modal_input_tel" value={"11"} type="text" name="" id=""/>
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
                    <h2>База товаров</h2>
                    <a href=""  className="btn_new_client">Добавить товар</a>
                    <a href=""  className="btn_new_client">Новая продажа</a>
                </div>
                <div className="surch">
                    <input className="surch_input" placeholder={"Поиск товаров (по наименованию или категории)"} type="text" name="" id=""/>
                    <a href=""  className="btn_surch">Поиск</a>
                </div>
                <p className="clients_nbr"> 5 <span className="clients_nbr_text">записей о товарах:</span></p>

            </div>
            <div className="wrap_wrap">
                <div className="clients_main">
                    <div className="table_test">
                        <tr className="sorting_wrap">
                            <input className="check" type="checkbox"/>
                            <td className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">Наименование</p></td>
                            <td className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">Количество в наличии</p></td>
                            <td className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">Цена за единицу</p></td>
                            <td className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">Категория</p></td>
                            <td className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">Количество заказов</p></td>
                        </tr>
                        <tr className="client_table_item first clients_table">
                            {/*класс first для первого элемента с классом client_table_item*/}
                            <input className="check"  type="checkbox"/>
                            <td className="client_inform_text"
                                onClick={() => {
                                    setClientId(1)
                                }}
                            >
                                Шапка вязаная “Балаклава"<img  className="edit_img" src={edit} alt=""/>
                            </td>
                            <td className="client_inform_nbr">15</td>
                            <td className="client_inform_nbr_bold">1570 ₽</td>
                            <td className="client_inform_text">handmade</td>
                            <td className="client_inform_nbr_bold">0</td>
                        </tr>
                        <tr className="client_table_item clients_table">
                            <input className="check"  type="checkbox"/>
                            <td className="client_inform_text"> Шапка вязаная “Балаклава"<img  className="edit_img" src={edit} alt=""/></td>
                            <td className="client_inform_nbr">15</td>
                            <td className="client_inform_nbr_bold">1570 ₽</td>
                            <td className="client_inform_text">handmade</td>
                            <td className="client_inform_nbr_bold">0</td>
                        </tr>
                        <tr className="client_table_item clients_table">
                            <input className="check"  type="checkbox"/>
                            <td className="client_inform_text"> Шапка вязаная “Балаклава"<img  className="edit_img" src={edit} alt=""/></td>
                            <td className="client_inform_nbr">15</td>
                            <td className="client_inform_nbr_bold">1570 ₽</td>
                            <td className="client_inform_text">handmade</td>
                            <td className="client_inform_nbr_bold">0</td>
                        </tr>
                        <tr className="client_table_item clients_table">
                            <input className="check"  type="checkbox"/>
                            <td className="client_inform_text"> Шапка вязаная “Балаклава"<img  className="edit_img" src={edit} alt=""/></td>
                            <td className="client_inform_nbr">15</td>
                            <td className="client_inform_nbr_bold">1570 ₽</td>
                            <td className="client_inform_text">handmade</td>
                            <td className="client_inform_nbr_bold">0</td>
                        </tr>
                        <tr className="client_table_item last clients_table"> {/*класс last для послднего элемента с классом client_table_item*/}
                            <input className="check"  type="checkbox"/>
                            <td className="client_inform_text"> Шапка вязаная “Балаклава"<img  className="edit_img" src={edit} alt=""/></td>
                            <td className="client_inform_nbr">15</td>
                            <td className="client_inform_nbr_bold">1570 ₽</td>
                            <td className="client_inform_text">handmade</td>
                            <td className="client_inform_nbr_bold">0</td>
                        </tr>
                    </div>

                </div>
                <div className="clients_side">
                    <div className="clients_side_card">
                        <p className="clients_side_card_title">Действия</p>
                        <p className="clients_side_card_subtitle">Операции</p>
                        <a href=""  className="clients_side_card_btn_blue"> <img  className="bin_img" src={bin} alt=""/>Удалить выбранных</a>
                        <a href=""  className="clients_side_card_btn_gray"> <img  className="bin_img" src={bin} alt=""/>Удалить всех найденных</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
}


export default Products