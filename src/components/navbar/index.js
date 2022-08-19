import React, { useContext, useState} from "react";
import { Navigate } from "react-router-dom";
import { Link } from "react-router-dom";

const Navbar = () => {

  const [usuario, setusuario] = useState(null);


//   function handleSubmit(event) {
//     event.preventDefault();
//     try {
//       let user = await login(event.target);
//       this.setState({ user });
//     } catch (error) {
//       this.setState({ error });
//     }
//   }
 console.log(<Navigate to='/login' replace={true}/>);

  return (


    <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
    <a href="http://localhost:3000/"  class="navbar-brand">LogoCompany</a>
        <button type="button" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
            <div class="navbar-nav">
                <a href="http://localhost:3000/" class="nav-item nav-link active">Inicio</a>
                <a href="http://localhost:3000/productos" class="nav-item nav-link">Productos</a>
                
            </div>
            <div class="navbar-nav ms-auto">
            <a href="http://localhost:3000/login"  class="nav-item nav-link">Login</a>
            </div>
        </div>
    </div>
</nav>


    
  );
};


export default Navbar;



