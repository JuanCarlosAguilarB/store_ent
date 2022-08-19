import React from 'react'
import  {useFetch} from '../../../hooks/useFetch';

const Cards = () => {
    let url = 'http://127.0.0.1:8000/api/v1/productos/'
    let data, isPending, error =useFetch(url);

  return (
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
  )
}

export default Cards