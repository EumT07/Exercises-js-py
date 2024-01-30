//String
let first_name: string = "Eublan";
let car: string = "Ford Mustang";
let last_name: string = "Mata";

//Number
let number: number = 30;
let age: number = 30;

//Boolean
let trueOrFalse: boolean = false;
let completed:boolean = true;


//Any : it can accept wahtever data type: string number wahtever

let newString: string ;

function getNewString(){
    return "Eublan"
    // return 45 //It doesn't work
}

newString = getNewString();


//Creating a security variable

let greetings: "Good Morning" | "Good evening" | "Good afternoon"

greetings = "Good Morning";




export {}
