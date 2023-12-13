"use strict"

//Escribir stream

const readline = require("readline");
const fs = require("fs");

//Example

const ask = readline.createInterface(process.stdin, process.stdout);

ask.question("Name of the folder ?\n", (name)=>{
    let stream = fs.createWriteStream(`./${name}.txt`, "utf-8");
    
    stream.write(`This folder: ${name} has the following trunk: \n`);

    process.stdout.write("Tell us more: \n");

    ask.on("line", (type)=>{

        let exit = "exit";
        
        if(type === exit){
            stream.close();
            ask.close();
        }else{
            stream.write(type.trim() + "\n");
        }
    });
});