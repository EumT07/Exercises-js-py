"use strict"

// FEcth API - Brwoser API for http ( AJAX) request
//Default - GET Request, supports other methods as well 
// Returns Promise

const url = "https://www.course-api.com/react-tabs-project";
const url2 = "https://www.course-api.com/react-store-products";

// With Fecth
// fetch(url)
//     .then(response => response.json())
//     .then(data => console.log(data))
//     .catch(error => console.log(error))


// with Async

const getData = async ()=>{
    try {
        const resp = await fetch(url2)
        const data = await resp.json()
        // console.log(data);
        return data
    } catch (error) {
        console.log(error)
    }
}

const result = getData();
// console.log(result.then(data => console.log(data)))


// If you have an error

const url3 = "https://www.course-api.com/react-tours-projects";

const getTours = async () => {
    try {
        const resp = await fetch(url3)
        // console.log(resp);

        //throw new  error

        if(!resp.ok){
            const message = "There is an error with the response " + resp.status + " and " + resp.statusText
            throw new Error(message)
        }

        const tours = await resp.json()
        console.log(tours);
    } catch (error) {
        console.log(error.message);
    }
}

getTours()






