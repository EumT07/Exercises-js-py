import puppeteer from "puppeteer";
import util from "node:util";
import * as fs from 'fs'

const sleep = util.promisify(setTimeout);


const init = async () => {
    //* browser
    const browser = await puppeteer.launch({
        headless: false,
        slowMo: 500
    });
    //* Open new page
    const page = await browser.newPage();
    //* URL
    // const url = "https://accounts.google.com/v3/signin/identifier?authuser=2&continue=https%3A%2F%2Fmail.google.com&ec=GAlAFw&hl=es&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S520497639%3A1699818506670327&theme=glif";
    const url = "https://www.facebook.com/";
    await page.goto(url);

    //* Email
    await page.waitForSelector("#email");
    await page.type("#email", "eublan_007@hotmail.com");
    await sleep(1000);

    //* Password
    await page.waitForSelector("#pass",{
        visible: true,
        hidden: false,
    });

    await page.type("#pass","eu.ve.blan.96");
    await sleep(1000);
    await page.click("[type='submit']");
    await page.waitForNavigation();



    await sleep(1000);
    //Cookies
    const cookies = await page.cookies();
    await fs.writeFile('./cookies.json', JSON.stringify(cookies, null, 2));
    // await browser.close();

} 

init()

