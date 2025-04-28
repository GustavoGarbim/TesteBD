import './App.css'
import Header from './pages/Header/Header'
import Conexao from './pages/Conexao/Conexao'
import Formulario from './pages/Formulario/Formulario'
import Footer from './pages/Footer/Footer'


function App() {

  return (
    <>
      <main className={'fundo'}>
        <Header />
        <Conexao />
        <Formulario />
        <Footer />
      </main>
    </>
  )
}

export default App
