"use strict"

/**
 * Muy util a la hora de crear un algoritmo para filtrar por categorias, se puede simplemente crer este algotimo y adaptarles unos etiquetas con htlml -tg button
 * 
 */

const cars = [
    {
        modelo: "Toyota",
        color: "Azul"
    },
    {
        modelo: "Chevrolet",
        color: "Blanco"
    },
    {
        modelo: "Ford",
        color: "Verde"
    },
    {
        modelo: "Toyota",
        color: "Gris"
    },
    {
        modelo: "Toyota",
        color: "Amarillo"
    },
    {
        modelo: "Ford",
        color: "Azul"
    },
    {
        modelo: "Chevrolet",
        color: "Azul"
    },
    {
        modelo: "Ford",
        color: "Azul"
    },
    {
        modelo: "Toyota",
        color: "Rojo"
    },
    {
        modelo: "Chevrolet",
        color: "Rojo"
    },
];

//Delearship

const models = cars.map(car => car.modelo);

console.log("All categories: ",models);


//Ussing set to gett unique values

const uniqueModels = new Set(cars.map(car => car.modelo));
const uniqueColors = new Set(cars.map(car => car.color));

console.log("Unique Values \"cars Models\"",uniqueModels);
console.log("Unique Values 'cars Colors\'",uniqueColors);

//Gettin list or an array

const allCategories_set = [...new Set(cars.map(car => car.modelo))];

console.log("Array of all models: ", allCategories_set);

//Adding a new string to our array
const tesla = "TesLa"
const allCategories2_set = [tesla,...new Set(cars.map(car => car.modelo))];

console.log("Array of all models with a new string: ", allCategories2_set);


