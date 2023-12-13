"use strict"
/**
 
 readdir 
 Lee la direccion y va mostrar todos los archivos que encuentre dentro de la carpeta asignada

 */

//readdirSync();
//readdir("string", callback())
//readFile("string", callback())

const fs = require("node:fs");

//Sync

// const files = fs.readdirSync("./");
// console.log(files);

//Async

fs.readdir("./", (err,data)=>{
    if(err){
        throw err
    }
    //Consulta todo lo que este dentro de la carpeta
    console.log(data);


    //Leer un archivo de manera Sync
    //readfileSync(Route,encode)
    const file = fs.readFileSync("./text.txt", "UTF-8");
    console.log(file);

    //Leer un archivo de manera Async

    fs.readFile("./text.txt", "UTF-8", (err, file) => {
        if(err){
            throw err
        }
        console.log(file);
    })
    
    console.log("Content")


});
