//// para que react sepa que esto es un hook, es necesario que empiece con use y lower camel case

import {useState,useEffect} from "react";

// no necesitamos el componente React, porque este no va a ser un componente funcional sino una funcion 
// como tal 
export const useFetch = (url) => {
  const [data, setData] = useState(null);
  const [isPending, setIsPending] = useState(true); // varriable que esta pendiente de si ya se realizó la petición
  const [error, setError] = useState(null);   // por si la solicitud fetch falla 

  useEffect(() => {
    const getData = async (url) => {
      try {
        let res = await fetch(url);

        if (!res.ok) {
          throw {
            err: true,
            status: res.status,
            statusText: !res.statusText ? "Ocurrió un error" : res.statusText,
          };
        }

        let data = await res.json();

        setIsPending(false);
        setData(data);
        setError({ err: false });
      } catch (err) {
        setIsPending(true);
        setError(err);
      }
    };

    getData(url);
  }, [url]);

  return { data, isPending, error };
};
