"use strict"

class Hamburger{
    constructor(burger,drink){
        this.burger = burger;
        this.drink = drink;
    }
    getFood(){
        return `Burger: ${this.burger} - Drink: ${this.drink}`
    }
};

let burger1 = new Hamburger("Chicken", "Coca-cola");
let burger2 = new Hamburger("Meat", "Pepsi-cola");

console.log("Type: ", burger1);
console.log("Type: ", burger2);

class ComboA extends Hamburger{
    constructor(burger,drink,combo = [],iceCream){
        super(burger,drink);
        this.combo = combo;
        this.iceCream = iceCream;
    };

    comboAInfo(){
        return super.getFood() + `Content: ${this.combo} pluss: ${this.iceCream}`
    };
};

let comboBurger = new ComboA("Meat and Chicken", "Orange", ["French Fries", "Ruffle"],"Chocolate and Straberry");

console.log(comboBurger);

//Setter and Getter dentro de un obejto
//set: Propierty
//getter: value

const datos = {
    
    //Set --> receive the value
    set location(valor){
        this._location = valor;
    },
    //get --> Assign the value
    get location(){
        return this._location
    }
}

//Set: enviamos la informacion
let pais1 = datos.location = "Venezuela";
let pais2 = datos.location = "España";

//fuera de contexto pero enviamos el object a una funcion
const pais = function country(pais1){
    return datos.location;
 };

//console.log(datos);
console.log(pais());
console.log(pais1);
console.log(pais2);

//Setter and getter nuestra classes

class Person2 {
    constructor(name, lastName){
        this.name = name;
        this.lastName = lastName;
    };
};

class otherPerson extends Person2{
    constructor(name, lastName){
        super(name, lastName);
    };

    //set
    set years(age){
        return this._edad = age;
    }
    //get
    get years(){
        return this._edad;
    }
    
}

const PERSON_ONE = new otherPerson("Juan Luis", "Guerra");
console.log(PERSON_ONE);
//Enviamos la nueva edad
PERSON_ONE.years = 40;
console.log(PERSON_ONE);