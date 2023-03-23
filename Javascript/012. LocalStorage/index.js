"use strict"

//The localStorage read-only property of the window interface allows you to access a Storage object for the Document's origin; the stored data is saved across browser sessions.

//LocalStorage: Almacenamiento local del ordenador, permite guardar pequeños datos en el almacenamiento del ordenador para poder mantener una session activa, o guardar cierto tipo de datos no sensibles

//Se recomienda evitar este metodo para guardar contraseñas o informacion privada.

//Set item: similar to creat a obj: key and values

localStorage.setItem("user", "Luisito");

//getItem
localStorage.getItem("user");

/* 
    Methods

    .remover(); Delete all items
    .clear(); Clean all data

*/

localStorage.removeItem("user");
localStorage.clear()

// JSON 

const user = {
    name: "The Crow",
    edad: 28
}

//Setting: JSON

// Object --> JSON.strigify --> String

const userJSON = JSON.stringify(user);

//Saving data insede the web page (localstorage)

localStorage.setItem("user", userJSON);

//Getting: JSON

const get_UserJSON = localStorage.getItem("user")

//String --> JSON.parse() --> Object

const userOb_JSON = JSON.parse(get_UserJSON);


//SessionSorage

// Save data to sessionStorage
sessionStorage.setItem("key", "value");

// Get saved data from sessionStorage
let data = sessionStorage.getItem("key");

// Remove saved data from sessionStorage
sessionStorage.removeItem("key");

// Remove all saved data from sessionStorage
sessionStorage.clear();


//Cookies

//crear: document.cookie = "nombre=Eublan" //key=value

//caducidad: 
//document.cookie = "nombrecaducidad=nombre;expires=" + new Date(2023,0,1).toUTCString()