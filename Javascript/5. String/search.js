//Search and text Editing Methods

/**
 * Part I: It allows us to search the index position of any words
 * 
 *          indexof():
 *          lasIndexOf()
 *          search()
 *          match()
 *          chartA()
 * 
 **/
console.log("* * * Part I * * *\n");
let text = "There is a big house, between that mountains and that green forest, they look amazing";

//Index OF
let result_indexOf = text.indexOf("that"); // 30

//Last Index Of
let result_lastIndexOf = text.lastIndexOf("that"); // 49

//Search
let word1 = "between";
let result_search = text.search(word1);

//Match
let word2 = "mountains";
// let result_match = text.match(word2);

//ChartAt: we need to insert a number (index) and it will return us the chart in that position
let result_chartAt = text.charAt(25);

console.log("< < < Result: Search Methods > > >");
console.log("Text Length: ",text.length);
console.log("\tIndexof: the First 'That' is in the position: ", result_indexOf);
console.log("\tLastIndexOf: the Last 'That' is in the position: ",result_lastIndexOf);
console.log(`\tSearch: The word -> '${word1}' is in the position: `,result_search);
// console.log(`\tMatch: The word -> '${word2}' is in the position: `,result_match);
console.log(`\tChartAt: 'bet-w-een' we insert 25 and we got w: `,result_chartAt);


//Part II: It allows know is any string has any words, letter o numbers inside it.

console.log("\n* * * Part II * * *\n");
let message = "Today, is a beautiful day, so for that reason I'm going to the beach";

console.log("startwith(): ",message.startsWith("Today"));
console.log("endswith(): ",message.endsWith("beach"));

//Include
//@param searchString — search string
//@param position — If position is undefined, 0 is assumed, so as to search all
console.log("includes(): ",message.includes("is", 8));

// Part III: Methods to replace, subtring, slice, split and trim text
/**
 * repeat()
 * replace()
 * slice()
 * substring()
 * split()
 * trim()
 * 
*/

console.log("\n* * * Part III * * *\n");

// Repeat()
let stringText = " Hello ";
let result_A = stringText.repeat(4);
console.log("repeat(): ",result_A);

//replace()
let stringText2 = "I'm learning javascript";
let result_B = stringText2.replace("javascript", "python");
console.log("replace(): ",result_B);

//slice(start,end)
//start: it starts counting and cuttingt the text
//end: the last position when finishes counting
let stringText3 = "This text is going to be a little bit short than few minutes ago";

let index_1 = stringText3.indexOf("bit");
console.log(index_1);
let result_C = stringText3.slice(index_1, 44);
console.log("slice(): ",result_C);

//substring(start,end)
let stringText4 = "You can flay";//can 
let result_D = stringText4.substring(4,7);
console.log("substring(): ",result_D);

//Split: Transform string into an array
let stringText5 = "Hello my friend today I'm going to tell you something really important";
let result_E = stringText5.split(' ');
console.log("split(' '): ",result_E);

let stringText6 = "Hello-my-friend-today-I'm-going-to-tell-you-something-really-important";
let result_F = stringText6.split("-");
console.log("split('-'): ",result_F);

//trim(): it deletes any space
let message2 = "     hola     ";

//trimStart(): it deletes any space at start of the text 
console.log("trimStart():",message2.trimStart());

//trim(): it deletes any space both start/end
console.log("trim():",message2.trim());

//trimEnd(): it deletes any space at the end of the text 
console.log("trimEnd():",message2.trimEnd());