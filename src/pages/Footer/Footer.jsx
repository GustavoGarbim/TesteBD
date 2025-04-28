import Styles from './Footer.module.css'

function Footer() {
    return (
        <footer className={Styles.footer}>
            <div className={Styles.logo_ascend}>
                <h2>ASCEND</h2>
                <div className={Styles.paragrafo_ascend}>
                    <p>Conectando iniciantes em tecnologia a oportunidades de crescimento.</p>
                </div>
            </div>
            <div className={Styles.navegacao}>
                <h3>Navegação</h3>
                <ul>
                    <li><a href="#">Início</a></li>
                    <li><a href="#">Cursos</a></li>
                    <li><a href="#">Eventos</a></li>
                    <li><a href="#">Quiz</a></li>
                    <li><a href="#">Fórum</a></li>
                    <li><a href="#">Planos</a></li>
                </ul>
            </div>
            <div className={Styles.contato}>
                <h3>Contato</h3>
                <p><i class="bi bi-envelope"></i>contato@ascend.com.br</p>
                <p>(11) 96161-6161</p>
            </div>

            <div className={Styles.redes_sociais}>
                <h3>Redes Sociais</h3>
                <a href="#"><i class="bi bi-whatsapp"></i></a>
                <a href="#"><i class="bi bi-linkedin"></i></a>
                <a href="#"><i class="bi bi-github"></i></a>
            </div>
        </footer>
    )
}

export default Footer