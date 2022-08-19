import React from 'react'
// import { Link } from "react-router-dom";
// import { useHistory } from 'react-router-dom';


export default function Inicio() {
    // let history = useHistory();

    // const redirect = () => {
    //   history.push('/productos');
    // }

    return (
    // <>   
    //         <Link to="/">
    //         <h1>home</h1>
    //         </Link>
    //         <Link to="/productos">
    //         <h1>Productos</h1>
    //         </Link>
          
    //    </>
        


  <div class="p-3 p-md-5 m-md-3 text-center bg-light d-flex p-2 ">
    <div class="col-md-5 p-lg-5 mx-auto my-5">
      <h1 class="display-4 fw-normal">Punny headline</h1>
      <p class="lead fw-normal">And an even wittier subheading to boot. Jumpstart your marketing efforts with this example based on Apple’s marketing pages.</p>
      {/* <a class="btn btn-outline-secondary" href="/ha">Coming soon  <button onClick={redirect}>Redirect</button></a>
      
      <button >Redirect</button> */}

    </div>
    <div class="product-device shadow-sm d-none d-md-block"></div>
    <div class="product-device product-device-2 shadow-sm d-none d-md-block"></div>
    <img alt='casa' src="https://images.vexels.com/media/users/3/223365/isolated/preview/6b2a7030316c935702dc23b4d383809d-edificio-de-tienda-plano.png" />
    
  </div>


    )
}
