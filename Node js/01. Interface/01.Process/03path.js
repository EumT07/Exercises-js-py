"use strict"
const path = require("node:path");

console.log(__dirname);//Carpeta


console.log(__filename);//Archivo

//Basename: Devuelve solo el nombre del archivo 
console.log(path.basename(__filename));

//Une rutas
console.log(path.join(__filename));

// unir rutas con path.join
const filePath = path.join('content', 'subfolder', 'test.txt')
console.log(filePath);


/*

import { fileURLToPath } from "node:url";

//Start with a function

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

*/
