"use stritc"
const readline = require("node:readline");
const util = require("node:util");



// readline, Permite manipular el input and output
//createInterface : permite crear una interface
//process.stdin: Entrada 
//process.stdout: Salida
//process.exit(): Termina el proceso 
//setPropt(): Permite escribir en la consola, siempre y cuando escribas .prompt()
//.on = crea eventos

const rl = readline.createInterface(process.stdin, process.stdout);

// rl.question("What is your name: \n", (res) => {
//     console.log("Hola :\n" + res);
//     process.exit();
// });

const person = {
    name: " ",
    comments: []
};

rl.question("what is your name: \n", (resp)=>{
    person.name = resp;
    rl.setPrompt("Tell me any comment: \n");
    rl.prompt();

});

//On --> Evento Line
rl.on("line", (input) => {
    
    if(input.trim() === "exit"){
        //%s : string
        //%j : objetos JSON
        let message = util.format("Te llamas %s y esto me dijiste %j", person.name, person.comments);
        console.log(message);
        process.exit();
    } 
    person.comments.push(input.trim());

    rl.setPrompt("Tell me more: \n");//Escribe un output, pero no se va a escribir en la consola hasta 
    rl.prompt();//Uses this method

});