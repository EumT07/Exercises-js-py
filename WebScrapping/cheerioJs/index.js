import cheerio from "cheerio";
import fetch from 'node-fetch';
import fs from "node:fs";

const csv = fs.createWriteStream('quoates.csv',"utf-8");

async function scrap(params) {
    const response = await fetch("http://quotes.toscrape.com/");
    const html = await response.text();

    //Cheerio
    const $ = cheerio.load(html);

    //Getting title
    const webSite_tittle = $("title");

    //Getting h1
    const h1_text = $("h1");

    //Getting all quotes
    const qoutes = $(".quote").find("a");

    //Cacthing div container
    const div_row = $(".row .col-md-8").children();

    //gettin all elemento with the same class.
    //#1
    // const quotes = $(".quote span.text").each((i, el) => {
    //     // console.log(i, $(el).html());
    //     const quote_text = $(el).html();
    //     const quote = quote_text.replace(/(^\“|\”$)/g,"");
    //     console.log(i, quote);
    // })

    //#2

    // csv.write('Qoute|Author|Tags\n');
    $(".quote").each((i, el)=> {
        const quote_text = $(el).find("span.text").text().replace(/(^\“|\”$)/g,"");
        const author = $(el).find("span .author").html();
        const tags = [];
        $(el).find(".tags a.tag").each((i,el) => tags.push($(el).text()));

        // console.log(`
        // N°: ${i + 1}
        // Phrase: ${quote_text}
        // Author: ${author}
        // Tags: ${tags}`);

        //Excel file
        // csv.write(`${quote_text}|${author}|${tags}\n`);

    });

    
    //Showing into console
    // console.log(webSite_tittle.html());
    // console.log(h1_text.text().trim());
    // console.log(qoutes.html());
    // console.log(div_row.html());
}

scrap();