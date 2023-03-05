"use strict"

const teacher = {};

//Property
Object.defineProperty(teacher,"name",{value: "Eublan"});

//Properties
Object.defineProperties(teacher, {
    lastname: {value:"Mata"},
    age:{value: 30}
});

//out
console.log(teacher.name);
console.log(teacher.lastname);
console.log(teacher.age);

//============================================
//Constructor Function 
//============================================

function Student(firstname,lastname,age,) {
    this.firstname = firstname;
    this.lastname = lastname;
    this.age = age;
}

let stundet_1 = new Student("Carlos", "Peluche",25);
let stundet_2 = new Student("Miguel", "Peluche",26);


//Add function
stundet_2.fullname = function(){
    return `${this.firstname} ${this.lastname}`
}

//Add to construct function
Student.prototype.getName = function(){
    return `My name is ${this.firstname}`
}

console.log(stundet_1);
console.log(stundet_1.getName());
console.log(stundet_2);
console.log(stundet_2.fullname());

//===============================
// inherit costructor function
//===============================

function Books(fisrtname,lastname,age,books = []){
    Student.call(this,fisrtname,lastname,age);
    this.books = books;
}

let studentAndBooks_1 = new Books("Andres","Perez",35,["face to face","English basic"]);

console.log(studentAndBooks_1);

//================================================================
// getters and setters
//Getter => access properties
//setter => change (mutate) properties
//================================================================

const album = {
    song1: "LA noche vieja",
    song2: "Año nuevo",
    get fullList(){
        return this.song1 + " " + this.song2
    },
    set fullList(value){
        const parts = value.split(" ");
        this.song1 = parts[0];
        this.song2 = parts[1];
    }
  
  };
  
  album.fullList = "Traicion Esmeralda";
  
  console.log(album.fullList);

//================================================================
// Creating a property with Asign
//================================================================

Object.assign(
    album,{
    artis:"Eublan",gen:"RockAndMetal"
});

console.log(album.artis)

