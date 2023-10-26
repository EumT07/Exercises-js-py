"use strict"
// const events = require("node:events");
// const emitter = new events.EventEmitter();
// const util = require("node:util");


//First part 
// sin heredar.

//Algo estilo setear y la llave
// emitter.on("eventCustom", (message, status) => {
//     console.log(`${status}: This is your message: ${message}`);
// })

// emitter.emit("eventCustom", "Hello my friend", 200);

//Second part
const eventEmitter = require("events").EventEmitter;
const util = require("util");

let Person = function(name){
    this.name = name;
}

util.inherits(Person, eventEmitter);// it allow you inherit all propietty and it could be uses. 

let person = new Person("Eublan");

person.on("talking", (message)=> {
    console.log(`${person.name}: ${message}`);
})

person.emit("talking", "Today is a great day");