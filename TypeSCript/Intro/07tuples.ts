const user: (string | number)[] = [2,"hello"]
let user2: [string, number, boolean];

// user2 = [true,"hola",23] //Wrong
user2 = ["hello",23,false] 

//With type
type User3 = [number,string]

const newUser: User3 = [23,"hola"];

newUser[1] = "nuevo String";

