import puppeteer from "puppeteer";
import path from "path";
import * as fs from 'fs'

const init = async () => {
  const browser = await puppeteer.launch({
    headless: false,
  });
  const page = await browser.newPage();

  //load cookies
  const cookiesString = await fs.readFile("pucookies.json");
  const cookies = JSON.parse(cookiesString);
  await page.setCookie(...cookies);

  const url = "https://www.facebook.com/";
    await page.goto(url);

  //await browser.close();
};

init();