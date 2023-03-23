"use strict"
/**
 * 
try– We put the test code inside the try statement block.

catch– if the test code fails, the catch block helps to handle the error.

throw– Let’s you make custom errors.

finally– This block executes at the end of the try catch regardless the test code throws an error or not.


An error can be of two types-

Coding or programming error made by the programmer.

Wrong input or any other error.


* 
 */

try{

    // test code goes here
  
}catch(err){
  
    // if test code throws error 
    // catch it and display the error
  
}finally{
  
    // put additional code 
    // which does not depends on the test code
    // or display a message simply
  
}

//                 Example 
try {
    let x = "eublan";
    let result = y + x;
} catch (err) {
    console.log("There is an error: ");
    console.log(
        "Error Name: " + err.name + "\n" + 
        "Error Message: " + err.message);
} finally {
    console.log("We finish");
}


/**

The error object contains two useful properties-
name      – returns an error name
message – returns an error message of type string 

Err name :

EvalError  – An error has occurred in the eval() function
RangeError  – A number “out of range” has occurred
ReferenceError – An illegal reference has occurred
SyntaxError – A syntax error has occurred
TypeError – A type error has occurred
URIError – An error in encodeURI() has occurred

*/

//***************************************** */
//       1 : Javascript Error
//***************************************** */
try {
    let num = 0;
    process.stdout.write(num);
} catch (err) {
    console.log(
      "Error Name: " + err.name + "\n" + 
      "Error Message: " + err.message);
} finally {
    console.log("---- End of execution----");
}

//***************************************** */
//          2: ReferenceError
//***************************************** */
try {
    console.log(num);
} catch (err) {
    console.log(
      "Error Name: " + err.name + "\n" + 
      "Error Message: " + err.message);
}

//***************************************** */
//          3: URIError
//***************************************** */
let num =-1;
try {
 if(num<0){
  throw new RangeError("number is negative");
 } 
} catch (err) {
  console.log(
    "Error Name: " + err.name + "\n" + 
    "Error Message: " + err.message);
}

//***************************************** */
//            4:SyntaxError
//***************************************** */
try {
    eval('Hey Hi!!');
} catch (err) {
    console.log(
      "Error Name: " + err.name + "\n" + 
      "Error Message: " + err.message);
}