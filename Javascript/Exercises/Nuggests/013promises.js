"use stritc"

// Javascript Nuggets - Promises

// async await
// consume/use promises

// Pending, Rejected, FulFilled
// const value = 2;
// const promise = new Promise((resolve,reject)=>{
//     const random = Math.floor(Math.random() * 3);
//     console.log(random);
//     if(random === value){
//         resolve("You guessed correctly");
//     }else{
//         reject("Wrong number");
//     }
// });

// promise
//     .then((data) => {console.log(data)})
//     .catch(error => console.log(error))

//Promises Sequence

//  Javascript Nuggets - Promises Example
// .first - after 1s first red;
// .second - after 3s second blue; 4s
// .third - after 2s third green; 6s
// IN SEQUENCE !!!!


const btn = document.querySelector('.btn');



btn.addEventListener("click",()=>{
    addColor(1000,".first","red")
        .then(()=> addColor(3000,".second","blue"))
        .then(() => addColor(6000,".third","pink"))
        .catch(error => console.log(error))
})

function addColor(time,selector,color) {
    const element = document.querySelector(selector)
    return new Promise((resolve,reject)=>{
        if(element){
            setTimeout(()=>{
                element.style.color = color
                resolve()
            },time)
        }else{
            reject(`There is an error: this ${selector} doesn't exist`)
        }
    })
}