import Styles from './Recentes.module.css'

function Recentes({texto_tech}){

    return(
        <button type='button' className={Styles.container}>
            <h2 className={Styles.texto}>{texto_tech}</h2>
        </button>
    )
}

export default Recentes