// asignando cualquier valor a una variable

let score : number | string = 33;

score = "45";

//Type
type User = {
    name: string,
    age: number
}
type Admin = {
    username: string,
    age: number
}
//Se puede utilizar alguno de los dos, se da la opcion de poder tener diferentes formas 
let helloUser: User | Admin = {name:"eublan",age: 30};

helloUser = {username: "Eublan",age:30}


//Function

function getId(id: number | string) {
    return `This is your id: ${id}`
}

getId("hola");
getId(34);

//Aplicando metodos
function metodos(value: number | string) {
    if(typeof value === "number"){
        return value + 4;
    }
    return value.toLowerCase();
}
metodos(23);
metodos("Hola");
