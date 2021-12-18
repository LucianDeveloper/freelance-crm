import React, {useEffect} from "react";
import './modal.scss'
import edit from "../../media/img/edit.svg";
import cross from "../../media/img/cross.svg";


const Modal = ({
                   visible = false,
                   title = '',
                   content = '',
                   footer = '',
                   onClose,
               }) => {
    // создаем обработчик нажатия клавиши Esc
    const onKeydown = ({key}) => {
        switch (key) {
            case 'Escape':
                onClose()
                break
        }
    }

    useEffect(() => {
        document.addEventListener('keydown', onKeydown)
        return () => document.removeEventListener('keydown', onKeydown)
    })


    // если компонент невидим, то не отображаем его
    if (!visible) return null;

    // или возвращаем верстку модального окна
    return <div className="modal" onClick={onClose}>
        <div className="modal-dialog" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
                <h3 className="modal-title">{title}</h3>
                <span className="modal-close" onClick={onClose}>
                    <img  className="cross_img" src={cross} alt=""/>
                </span>
            </div>
            <div className="modal-body">
                {content}
            </div>
            {
                footer && <div className="modal-footer">
                    {footer}
                </div>
            }
        </div>
    </div>
}

export default Modal
