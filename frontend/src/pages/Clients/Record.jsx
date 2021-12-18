import React from "react";
import edit from "../../media/img/edit.svg";


const Record = ({item, setClientId, index, maxIndex}) => {
    let style = "client_table_item clients_table";
    if (index === 0) {
        style += ' first'
    } else if (index === maxIndex) {
        style += ' last'
    }
    return <tr className={style}>
        <input className="check"  type="checkbox"/>
        <td className="client_inform_text"
            onClick={() => {
                setClientId(item.id)
            }}
        >
            {item.fio}
            <img  className="edit_img" src={edit} alt=""/>
        </td>
        <td className="client_inform_nbr">
            {item.phone}
        </td>
        <td className="client_inform_text">
            {item.url_tg}
        </td>
        <td className="client_inform_text">
            {item.url_inst}
        </td>
        <td className="client_inform_nbr_bold">
            1570 ₽
        </td>
        <td className="client_inform_nbr_bold">
            0 ₽
        </td>
    </tr>
}

export default Record