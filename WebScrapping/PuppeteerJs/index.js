/**
 * npm init -y
 * add "type" : "module" into package.json
 * npm install puppeteer@19.11.1
 */

import puppeteer from "puppeteer";
import fs from "fs/promises";
import radomUseragent from "random-useragent";

//fazt code

const init = async () => {
    const browser = await puppeteer.launch({
        headless: "new" // "new" ejecutar si mostrarse
    });

    const page = await browser.newPage();
    await page.setViewport({
        width: 1920,
        height: 1080
    });

    await page.goto("https://www.mercadolibre.com.ve/");
    await browser.close();
}

//Screeenshot
const screenshot = async () => {
    const browser = await puppeteer.launch({
        headless: "new"
    });
    const page = await browser.newPage();

    await page.goto("https://www.instagram.com/");
    await page.screenshot({
        path: "1shot.png"
    });
    await browser.close();
}


const getDataFromWeb = async () => {
    const browser = await puppeteer.launch({
        // headless: false, // "new" ejecutar si mostrarse
        headless: "new"
    });
    const page = await browser.newPage();

    await page.goto("https://example.com/");
    
    const result = await page.evaluate(()=>{
        const title = document.querySelector("h1").innerHTML;
        const description = document.querySelector("p").innerHTML;
        const more = document.querySelector("a").innerHTML;
        return {
            title,
            description,
            more
        }
    })


    console.log(result);
    await browser.close();
}

//Get data from quotes page

const getDataFrom_Quote = async () => {
    const browser = await puppeteer.launch({
        headless: "new"
    });

    //Start Page
    const page = await browser.newPage();

    await page.goto("https://quotes.toscrape.com/");

    const result = await page.evaluate(()=>{
        
        const quotes = document.querySelectorAll(".quote");
        
        const quoatesArray = [...quotes].map(quote => {
            const text = quote.querySelector(".text").innerHTML;
            const author = quote.querySelector(".author").innerHTML;
            const tags = [...quote.querySelectorAll(".tag")].map((tag)=>tag.innerHTML);
            return {
                text,
                author,
                tags
            }
        });
        return quoatesArray;
    });

    // console.log(result);
    await fs.writeFile("quotes.json", JSON.stringify(result,null,2));
    await browser.close();
}

// init();
// screenshot();
// getDataFromWeb();
getDataFrom_Quote();
