export class Render {
   constructor(containerID) {
      this.container = document.getElementById(containerID);
   }

   fetchData(URI, cb, options = {}) { /* Proceso a realizar con los datos. Le pasamos la dirección de los datos, una f callback para hacer algún proceso sobre esos datos a renderizar y opciones, que en forma predeterminada serán nulas */
      fetch(URI, options) /* Obtengo los datos */
         /* luego por medio de promesas: */
         .then((res) => res.json()) /* respuesta obtenida la convierto en json */
         .then((data) => { /* Luego, a la data recibida transformada en json, le aplico la función de colback para procesarla */
            if (!cb) { /* si no hay función de callback, registro la data por consola y devuelvo 'null' */
               console.log(data);
               return null;
            }

            let itemsRenderizar = cb(data); /* alamaceno la data resultante del callback en itemsRenderizar */
            this.#renderInContainer(itemsRenderizar); /* método interno al que le paso los items a renderizar */
            return;
         })
         .catch((error) => console.log({ error }));
   }
   #renderInContainer(items) { /* creamos el método interno con parámetro 'items a renderizar' */
      this.container.innerHTML = items; /* le pasamos al contenedor declarado los items como innerHTML */
   }
}
