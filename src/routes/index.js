import ReactDOM from "react-dom/client";
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";


import Login from "../components/pages/login";

//acá iremos colocando cada una de las rutas que vayamos usando
 const RoutesComponent = () =>{
    return (
        
        <BrowserRouter> 
            <Routes>
                {/* <Route path="/login" element={<Login/>} /> */}
                
            </Routes>
        </BrowserRouter>

    );
}

export default RoutesComponent;