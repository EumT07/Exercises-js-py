//Process:
//Permite imprimir en el terminal
const process = require("node:process")

/*

- process.stdout.write: Escribe en la consola

- process.stdin.on : Permite mostrar datos de salida. 

- process.exit(): Salir

- process.cwd() : current working directory

- process.env : variable entorno

*/ 

//Ejm

function first_example() {
    //Para escribir en pantalla
    process.stdout.write("What is your name: ");

    //Para leer un dato o recibir 
    // stdin : permite obtener datos
    // on: es un evento que va realizar

    process.stdin.on("data", (data) =>{
        const name = data.toString().trim();

        process.stdout.write(`Hello ${name} welcome to our app.`);
        process.exit();
    });
}

function second_example() {
    const questions = [
        "Hello, What is your name..?: ", 
        "How old are you..?: ", 
        "Whay are you writing to me..?: ", 
        "What do you need from me..?: "];
    
    function appQuestion(i){
        process.stdout.write(questions[i]);
    }
    
    const answers = []; // = 0
    process.stdin.on("data", (data)=>{
        answers.push(data.toString().trim());// = 1,
    
        if(answers.length < questions.length){
            appQuestion(answers.length);
        }else{
           for(let i=0; i < answers.length; i++){
            process.stdout.write(`
            Question ${i+1}: ${questions[i]} : ${answers[i]}`)
           }
            process.exit();
        }
    });
    
    appQuestion(0);
}

first_example()
second_example()