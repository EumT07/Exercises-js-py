"use strict"

const cart = [
    {
        title: "Samsung",
        price: 120.50,
        amount: 5},
    {
        title: "Nokia",
        price: 89.54,
        amount: 4},
    {
        title: "Blue3",
        price: 100.214,
        amount: 8},
    {
        title: "Samsun 34",
        price: 250.214,
        amount: 3},
    {
        title: "Nokia Af",
        price: 320,
        amount: 4
    },

]

// #1
const total = cart.reduce((total,items)=>{
    total += items.price * items.amount;
    return total;
},0);

console.log(total); //3786

// #2
const total2 = cart.reduce((total,items)=>{
    const {amount,price} = items;
    //Count items
    total.totaItems += amount;
    //Count :sum
    total.cartTotal += amount * price;
    return total;
},{
    totaItems:0,
    cartTotal:0
});

console.log(total2); // { totaItems: 24, cartTotal: 3786 }

//3 Destructuring
let {totalItems, cartTotal } = cart.reduce((total,items)=>{
    const {amount,price} = items;
    //Count items
    total.totalItems += amount;
    //Count :sum
    total.cartTotal += amount * price;
    return total;
},{
    totalItems:0,
    cartTotal:0
});
cartTotal = cartTotal.toFixed(1);
console.log(`
Products\n
\t N° Items: ${totalItems}
\t Total: ${cartTotal}  
`); 
