import Styles from './Recentes.module.css';

function Recentes({ texto_tech, onFiltrar }) {
    return (
        <button type="button" className={Styles.container} onClick={() => onFiltrar(texto_tech)}>
            <h2 className={Styles.texto}>{texto_tech}</h2>
        </button>
    );
}

export default Recentes;
