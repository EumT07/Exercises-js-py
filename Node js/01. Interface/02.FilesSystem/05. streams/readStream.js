"use strict"

//Leer Stream

const fs = require("fs");


//1 Forma rapida de leer sin mucho contenido

// let content = fs.readFileSync("./logs.log", "utf-8");
// console.log(content);

// 2 Forma de leer usando stream

let stream = fs.createReadStream("./logs.log", "utf-8");

let data = "";

//Se ejecuta una vez, sirve para saber cuando inicia un proceso
stream.once("data", ()=>{
    console.log("Iniciando el stream ..\n");
});

stream.on("data", (chunk)=>{
    // console.log(`${chunk.length} |`)
    data += chunk;
})

stream.on("end", ()=>{
    console.log("Fin del stream..\n");
    console.log(data.length);
})

// stream.setEncodin("UTF8") //Permite agregar la codificacion

