//Search Methods

/**
 * Part I: It allows us to search the index position of any words
 * 
 *          indexof(): Return index position *Start*
 *          lasIndexOf()
 *          search() : search the string in the text
 *          match()
 *          chartA()
 * 
 **/

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


