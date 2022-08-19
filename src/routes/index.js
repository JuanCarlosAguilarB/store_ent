import ReactDOM from "react-dom/client";
import {
  BrowserRouter,
  Routes,
  Route,
  useRoutes,
} from "react-router-dom";


import Login from "../components/pages/login";
import Inicio from "../components/inicio";
import Productos from "../components/productos";
const Home = () => useRoutes([
    { path: "/home", element: <Inicio /> },
    { path: "/", element: <Inicio /> },
    { path: "/inicio", element: <Inicio /> }
  ]);


 const RoutesComponent = () =>{
    return (
        
        <BrowserRouter> 
        <Home/>
            <Routes>
                <Route path="/login" element={<Login/>} />
                <Route path="/productos" element={<Productos/>} />
            </Routes>
        </BrowserRouter>

    );
}

export default RoutesComponent;