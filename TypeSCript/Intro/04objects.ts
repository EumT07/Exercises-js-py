// const user = {
//     name: "Eublan",
//     lastName: "Mata",
//     age: 31,
//     email: "eublanmata@gmail.com"
// }

//1
// function createUser({name: String, isHuman: boolean}) {}

// createUser({name: "Eublan", isHuman: true});

//2 Returning something

// function createCourse():{name: String, price: number} {
//     return{name:"react", price: 34};
// }


//Objects

type User = {
    readonly id?: number;
    name: string;
    email: string;
    ishuman: boolean;
    isGreater?: boolean;
}

// "?" : permite hacer ver al typescript que eesa propiedad puede estar o no dentro de nuestra logica
//Tambien permite saber si algo esta o no, estilo como considional.
// Readonly es solo de lectura, no puedes reasignar o editarla. 


// #1
// function createUser(user: User): User {
//     return {name: "",email: "", ishuman:true}
// }

// createUser({name: "Eublan", email: "eublan@gmail.com", ishuman: true});


// #2
function createUser(user: User): User {
    const {name, email,ishuman} = user
    return {name, email, ishuman}
}

createUser({name:"Eublan",email:"eublan@gamil.com",ishuman:true});


export {}