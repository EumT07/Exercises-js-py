//Posicion de los argumentos
// obligatorio, opcional, por defecto

//Simple function

function addTwo(num: number){
    return num * 2
}

addTwo(2);

// Upper variable

function upperVal(value: string){
    return value.toUpperCase();
}
upperVal("eublan");


//Mixing types

function userLogin(name: String, age: number, human: boolean = true){
    return `Hola mi nombre es: ${name}, tengo ${age} años, soy humano: ${human}`
}

userLogin("Eublan", 30);


//Better way to write functions

//Simple function
// Va retornar un numero
function sum(num: number): number{
    return num * 2
    // return "hello"
}

sum(2);


//arrow functions

const getHello = (s: string):string => {
    return "Hello " + s;
}

getHello("Eublan")


//Using map
const heros = ["thor", "spiderman", "ironman"]
// const heros = [1, 2, 3]

heros.map((hero): string => {
    return `hero is ${hero}`
})

//Error message

function consoleError(errmsg: string): void{
    console.log(errmsg);
    
}
// never: no va retornar algo
function handleError(errmsg: string): never{
    throw new Error(errmsg);
}


//Funciones con objetos

function withObject({name, lastName, id}: {name:string, lastName:string, id:number}) {
    return `Hola ${name} ${lastName} con el id: ${id}`
}

withObject({name: "Eublan",lastName: "mata", id: 23454})


//Functiones callback

const greetingFunction = (callback: (name: string ) => void) => {
    callback("carro");
}

const vehiculo = (name: string) =>{
    return name;
}

greetingFunction(vehiculo)

export {}