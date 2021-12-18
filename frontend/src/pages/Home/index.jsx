import React from "react";
import news_img from "../../media/img/news_img.jpg";
import msp from "../../media/img/MSP.svg";
import msp2 from "../../media/img/msp.png";
import derbo from "../../media/img/derbo.svg";
import buisnes from "../../media/img/my-business.svg";


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
                            <div className="news_img_wrap"><img  className="news_img" src={news_img} alt=""/></div>
                        </div>
                        <div className="news_item">
                            <p className="news_title">Не облагаемый налогом доход по вкладам россиян увеличится до 85 тысяч рублей в 2022 году</p>
                            <p className="news_subtitle">Жители России, имеющие вклады в банках в общей сумме более 1 миллиона рублей, у которых процентный доход превышает 85 тысяч рублей...</p>
                            <div className="news_img_wrap"><img  className="news_img" src={news_img} alt=""/></div>
                        </div>
                        <div className="news_item">
                            <p className="news_title">Не облагаемый налогом доход по вкладам россиян увеличится до 85 тысяч рублей в 2022 году</p>
                            <p className="news_subtitle">Жители России, имеющие вклады в банках в общей сумме более 1 миллиона рублей, у которых процентный доход превышает 85 тысяч рублей...</p>
                            <div className="news_img_wrap"><img  className="news_img" src={news_img} alt=""/></div>
                        </div>
                        <div className="news_item">
                            <p className="news_title">Не облагаемый налогом доход по вкладам россиян увеличится до 85 тысяч рублей в 2022 году</p>
                            <p className="news_subtitle">Жители России, имеющие вклады в банках в общей сумме более 1 миллиона рублей, у которых процентный доход превышает 85 тысяч рублей...</p>
                            <div className="news_img_wrap"><img  className="news_img" src={news_img} alt=""/></div>
                        </div>

                    </div>

                </div>
                <div className="clients_side">
                    <div className="clients_side_card">
                        <p className="clients_side_card_title">Вид публикации</p>
                        <a href=""  className="news_side_card_btn_blue">Новости</a>
                        <a href=""  className="news_side_card_btn_blue">Статьи</a>
                        <a href=""  className="news_side_card_btn_blue">Документы</a>
                        <p className="clients_side_card_title2">Полезные ссылки</p>
                        <div className="useful_link">
                            <img  className="useful_link_img1" src={buisnes} alt=""/>
                            <a href="https://www.mb31.ru/" className="useful_link_text">Центр «Мой бизнес» Белгородской области</a>
                        </div>
                        <div className="useful_link">
                            <img  className="useful_link_img2" src={msp2} alt=""/>
                            <a href="https://corpmsp.ru/" className="useful_link_text">Поддержка малого и среднего предпринимательства (МСП)</a>
                        </div>
                        <div className="useful_link">
                            <img  className="useful_link_img3" src={derbo} alt=""/>
                            <a  href="http://www.derbo.ru/" className="useful_link_text">Департамент экономического развития Белгородской области</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
}


export default Home