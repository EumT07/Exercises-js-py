"user strict"

console.log("< < < - Aritmetic Operators - > > >\n");

/**
 * Operator: 
 *              Addition = +
 *              Subtraction = -
 *              Multiplication = *
 *              Division = /
 * 
        An arithmetic operator accepts numerical values as operands and  returns a single numerical value. The numerical values can be literals or variables.

 */

let add = 4 + 4; //--> 8
let sub = 4 - 2;//--> 2
let mult = 2 * 5;// --> 10
let div = 10 / 4;// --> 2.5

console.log(add);
console.log(sub);
console.log(mult);
console.log(div);

const num1 = 8;
const num2 = 2;

let add_result = num1 + num2;
let sub_result = num1 - num2;
let mul_result = num1 * num2;
let div_result = num1 / num2;

console.log(`
Addition: ${add_result}
Subtration: ${sub_result}
Multiplication: ${mul_result}
Division: ${div_result}
`);

/**
       JavaScript uses the % to represent the remainder operator. The remainder operator returns the remainder left over when one value is divided by another value.
 
       Modulo = %

*/

console.log("< < < - Module or remainder Operator - > > >\n");

let remainder1 = 5 % -2;
console.log(remainder1);

let remainder2 = 5 % 2;
console.log(remainder2);


/**
 * Comparison Operators
 * 
       To compare two values, you use a comparison operator. The following table shows the comparison operators in JavaScript:
       < : Less than
       > : Greater Than
       <= : Less than or equal to
       >= : Greater than or equal to
       == : equal to
       === : strict equal yo
       != : not equal
       !== : estrict not equal
 */

console.log("< < < - Comparison Operator - > > >\n");

let number_A = 8;
let number_B = 4;

//it will return true or false

let lessThan = number_A < number_B;
console.log(lessThan); //false

let greaterThan = number_A > number_B;
console.log(greaterThan); // true

let lessThan_equal = number_B <= 4;
console.log(lessThan_equal); // true

// compare to values

let string_Number = "23"
let number_Number = 23

// ==
const result_A = string_Number == number_Number;
console.log(result_A); // True

// ===
const result_B = string_Number === number_Number; 
console.log(result_B); // False

/* != */
const result_C = "user" != "User"; // True
console.log(result_C);

const result_D = "24" != 24 ; // False
console.log(result_D);

/* !== */
const result_E = "24" !== 24 ; // True
console.log(result_E);


console.log("< < < - Logic Operators - > > >");

// # And Rules 
console.log("And (&&) Operator");
// # true and true --> True
// # false and true --> False
// # true and false --> False
// # false and false --> False

let value1 = (24 > 8 && 12 > 9); // (true && true ) True
console.log(value1);
let value2 = ("miguel" == "miguel" && 12 <= 9); // (true && false ) false
console.log(value2);

// # Or rules
console.log("or (||) Operator");
// # true or true --> True
// # false or true --> True
// # true or false --> True
// # false or false --> False

let value3 = (24 > 8 || 12 > 9); // (true || true ) True
console.log(value3);
let value4 = ("miguel" == "miguel" || 12 <= 9); // (true || false ) true
console.log(value4);
let value5 = ("andres" == "miguel" || 12 >= 24); // (false || false ) false
console.log(value5);

// # Not Operator !
console.log(" ! Not Operator ");
console.log(!(true)); // False
console.log(!(false)); // True

// Asign Operator
console.log("< < < - Asing Operator - > > >");
// Simple =
let val_1 = 8;
let vale_2 = 4;

console.log("Valor inicial de val_1: "+ val_1);

// +=
console.log("Valor actual de val_1: "+ val_1);
let sum = val_1 += vale_2; // 12
console.log(sum);
// -=
console.log("Valor actual de val_1: "+ val_1);
let less = val_1 -= vale_2 // 4
console.log(less);

// *=
console.log("Valor actual de val_1: "+ val_1);
let multi = val_1 *= vale_2; // 10
console.log(multi);
// /=
console.log("Valor actual de val_1: "+ val_1);
let divid = val_1 /= 2 // 8
console.log(divid);

