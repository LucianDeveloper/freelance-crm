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
                    <h2>Новости и важная информация</h2>
                </div>
                <div className="surch">
                    <input className="surch_input" placeholder={"Поиск новости"} type="text" name="" id=""/>
                    <a href=""  className="btn_surch">Поиск</a>
                </div>
            </div>
            <div className="wrap_wrap">
                <div className="clients_main">
                    <div className="news_block">
                        <div className="news_item">
                            <p className="news_title">Не облагаемый налогом доход по вкладам россиян увеличится до 85 тысяч рублей в 2022 году</p>
                            <p className="news_subtitle">Жители России, имеющие вклады в банках в общей сумме более 1 миллиона рублей, у которых процентный доход превышает 85 тысяч рублей...</p>
                        </div>
                    </div>
                </div>
                <div className="clients_side">
                    <div className="clients_side_card">
                        <p className="clients_side_card_title">Вид публикации</p>
                        <a href=""  className="clients_side_card_btn_blue"> <img  className="telega_img" alt=""/>Новости</a>
                        <a href=""  className="clients_side_card_btn_blue"> <img  className="telega_img" alt=""/>Статьи</a>
                        <a href=""  className="clients_side_card_btn_blue"> <img  className="telega_img" alt=""/>Документы</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
}


export default Home