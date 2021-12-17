import React from "react";
import drop from "../../media/img/drop.svg";


const Clients = () => {
    return <div>
        <div className="clients_wrap">
            <div className="clients_main">
                <div className="new_client">
                    <h2>Клиентская база</h2>
                    <a href=""  className="btn_new_client">Добавить клиента</a>
                </div>
                <div className="surch">
                    <input className="surch_input" placeholder={"Поиск клиентов (по имени, email, телефону или данным мессенджеров)"} type="text" name="" id=""/>
                </div>
                <div className="clients_table_block">
                    <p className="clients_nbr">13 <span className="clients_nbr_text">записей найдено:</span></p>
                    <div className="sorting_wrap">
                        <input type="checkbox"/>
                        <div className="drop_item"><img  className="drop_img" src={drop} alt=""/> <p className="drop_text">ФИО/Название</p></div>
                    </div>
                </div>
            </div>
            <div className="clients_side">
                222
            </div>
        </div>
    </div>
}


export default Clients