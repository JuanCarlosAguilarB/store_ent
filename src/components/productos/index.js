import React from 'react'
// import {useFetch} from "../hooks/useFetch"
import "./index.css"


function Productos() {

  fetch('http://127.0.0.1:8000/api/v1/productos/')
  .then(response => response.json())
  .then(data => console.log(data));

  return (
    <section><div class="container">
    <div class="row gy-4">
        <div class="col-sm">
            <div class="card h-100">
                <img src="..." class="card-img-top" alt="..."/>
                <div class="card-body">
                    <h5 class="card-title fw-bold">Card title</h5>
                    <p class="card-text">Some quick example text to build make up the bulk of the card's content.
                    </p>
                </div>
            </div>
        </div>
        <div class="col-sm">
            <div class="card h-100">
                <img src="..." class="card-img-top" alt="..."/>
                <div class="card-body">
                    <h5 class="card-title fw-bold">Card title</h5>
                    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content. Some more quick example text for the card's content.</p>
                </div>
            </div>
        </div>
        <div class="col-sm">
            <div class="card h-100">
                <img src="..." class="card-img-top" alt="..."/>
                <div class="card-body">
                    <h5 class="card-title fw-bold">Card title</h5>
                    <p class="card-text">Some quick example text to make up the bulk of the card's content.</p>
                </div>
            </div>
        </div>
    </div>
</div></section>
  );
}

export default Productos;
