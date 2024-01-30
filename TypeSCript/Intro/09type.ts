//template union types
type hexadecimalColor =  `#${string}`;

// const color1:hexadecimalColor = "453sds"; Error
const color2:hexadecimalColor = "#453sds";

// Combinar types

type Userinfo = {
    name: string,
    lastname: string,
    age: number
}

type Usernotes = {
    score?: number,
    dni?: number
}

type Userunion = Userinfo & Usernotes


let person: Userunion = {
    name: "Eublan",
    lastname: "Mata",
    age: 31
};


//Si tenemos un tipo con un objeto interno, podemos acceder a su propiedad 

type CarProperties = {
    isOn: boolean,
    model: {
        brand: string,
        color: string
    }
}

const brandCard: CarProperties["model"] = {
    brand: "Mustang",
    color: "Black"
}