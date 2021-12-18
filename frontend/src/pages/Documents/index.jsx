import React,{useState} from "react";
import Modal from "../../components/Modal";
import drop from "../../media/img/drop.svg";
import edit from "../../media/img/edit.svg";
import bin from "../../media/img/bin.svg";
import load from "../../media/img/download.svg";


const Documents = () => {
    const [clientId, setClientId] = useState(null);
    return <div>


        <Modal title={''}
               content={
                   <div className="modal-content">
                       <p className="modal_title">Добавление документа</p>
                       <p className="modal_subtitle_center">Информация о документе</p>
                       <p className="modal_subtitle">Дата заключения договора</p>
                       <input className="modal_input_tel" value={"15.08.2021"} type="text" name="" id=""/>
                       <p className="modal_subtitle">Вид договора</p>
                       <input className="modal_input" value={"Купля-продажа"} type="text" name="" id=""/>
                       <p className="modal_subtitle">Описание</p>
                       <input className="modal_input" value={""} type="text" name="" id=""/>
                       <p className="modal_subtitle">Номер №</p>
                       <input className="modal_input_tel" value={"00001"} type="text" name="" id=""/>
                       <p className="modal_subtitle_center">Информация о клиенте</p>
                       <p className="modal_subtitle">ФИО</p>
                        <input className="modal_input" value={"Сивцев Сергей Михайлович"} type="text" name="" id=""/>
                       <p className="modal_subtitle">Серия номер паспорта</p>
                       <input className="modal_input_tel" value={"1420 101010"} type="text" name="" id=""/>
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
                    <h2>Документы</h2>
                    <button type="button"
                       className="btn_new_client"
                       onClick={() => {
                           setClientId(1)
                       }}
                    >
                        Добавить документ
                    </button>
                </div>
                <div className="surch">
                    <input className="surch_input" placeholder={"Поиск товаров (по наименованию или категории)"} type="text" name="" id=""/>
                    <a href=""  className="btn_surch">Поиск</a>
                </div>

            </div>
            <div className="wrap_wrap">
                <div className="clients_main">
                    <div className="table_test">
                        <tr className="sorting_wrap">
                            <input className="check" type="checkbox"/>
                            <td className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">Название документа</p></td>
                            <td className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">Описание документа</p></td>
                            <td className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">Номер документа</p></td>
                            <td className="drop_item"><img  className="load_img" src={load} alt=""/> <p className="drop_text">Скачать</p></td>

                        </tr>
                        <tr className="client_table_item first clients_table">
                            {/*класс first для первого элемента с классом client_table_item*/}
                            <input className="check"  type="checkbox"/>
                            <td className="client_inform_text">Договор купли-продажи...</td>
                            <td className="client_inform_text">Иванов Петр Сергеевич, покупка...</td>
                            <td className="client_inform_nbr">10009234</td>
                            <td><a href="#" className="client_inform_link">Скачать</a></td>
                        </tr>
                        <tr className="client_table_item  clients_table">
                            {/*класс first для первого элемента с классом client_table_item*/}
                            <input className="check"  type="checkbox"/>
                            <td className="client_inform_text">Договор купли-продажи...</td>
                            <td className="client_inform_text">Иванов Петр Сергеевич, покупка...</td>
                            <td className="client_inform_nbr">10009234</td>
                            <td><a href="#" className="client_inform_link">Скачать</a></td>
                        </tr>
                         <tr className="client_table_item  clients_table">
                            {/*класс first для первого элемента с классом client_table_item*/}
                            <input className="check"  type="checkbox"/>
                            <td className="client_inform_text">Договор купли-продажи...</td>
                            <td className="client_inform_text">Иванов Петр Сергеевич, покупка...</td>
                            <td className="client_inform_nbr">10009234</td>
                            <td><a href="#" className="client_inform_link">Скачать</a></td>
                        </tr>
                      <tr className="client_table_item  clients_table">
                            {/*класс first для первого элемента с классом client_table_item*/}
                            <input className="check"  type="checkbox"/>
                            <td className="client_inform_text">Договор купли-продажи...</td>
                            <td className="client_inform_text">Иванов Петр Сергеевич, покупка...</td>
                            <td className="client_inform_nbr">10009234</td>
                            <td><a href="#" className="client_inform_link">Скачать</a></td>
                        </tr>
                    <tr className="client_table_item last clients_table">
                            {/*класс first для первого элемента с классом client_table_item*/}
                            <input className="check"  type="checkbox"/>
                            <td className="client_inform_text">Договор купли-продажи...</td>
                            <td className="client_inform_text">Иванов Петр Сергеевич, покупка...</td>
                            <td className="client_inform_nbr">10009234</td>
                            <td><a href="#" className="client_inform_link">Скачать</a></td>
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


export default Documents