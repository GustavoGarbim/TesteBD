import Styles from './Header.module.css'

function Header() {

    return (
        <header className={Styles.header}>
            <div className={Styles.logo}>
                <h2>Ascend</h2>
            </div>
            <nav className={Styles.navigation}>
                <ul>
                    <li><a href="#">Cursos</a></li>
                    <li><a href="#">Eventos</a></li>
                    <li><a href="#">Quiz</a></li>
                    <li><a href="#">Fórum</a></li>
                    <li><a href="#">Planos</a></li>
                </ul>
            </nav>
            <div className={Styles.login}>
                <button>Login</button>
            </div>
        </header>
    )
}

export default Header