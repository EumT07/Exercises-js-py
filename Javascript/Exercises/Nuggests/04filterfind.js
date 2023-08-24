"use strict"

// Filter - returns a new array, can manipulate the size of new array (unlike map), returns based on condition

// Find - returns single instance (object), returns first match, if no match - undefined

const people = [
    { name: 'bob', age: 20, position: 'developer' },
    { name: 'peter', age: 25, position: 'designer' },
    { name: 'susy', age: 30, position: 'the boss' },
    { name: 'anna', age: 35, position: 'intern' },
  ];

// filter
const youngPeople = people.filter((person) => {
    return person.age <= 25;
});
console.log(youngPeople);

const developers = people.filter((person) => person.position === 'developer');
console.log(developers);

// filter: no match result

const seniorDevs = people.filter((item) => item.position === 'senior dev');
console.log(seniorDevs);//it returns an empty arry []

//Find
const peter = people.find((person) => person.name === 'peter');

console.log(peter);

//Find:  no match
const baker = people.find((person) => person.position === "baker");
console.log(baker); //it returns an undefined result

// multiple matches

//IT just return one items
const randomPerson = people.find((person) => person.age < 35);
console.log(randomPerson);

const anna = people.filter((person) => person.name === 'anna');
console.log(anna);

console.log(anna[0].position);