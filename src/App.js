import logo from './logo.svg';
import './App.css';
import Navbar from './components/navbar';
import Inicio from './components/inicio';
import Productos from './components/productos';
import Login from './components/pages/login';

import Routes from "./routes"
function App() {
  return (

    <div className="App">
      <Navbar/>
      <Routes></Routes>
    {/* <Navbar></Navbar>
    <Inicio></Inicio>
    <Productos></Productos>
    <Login></Login> */}
    </div>
  );
}

export default App;
