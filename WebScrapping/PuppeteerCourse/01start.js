import puppeteer from "puppeteer";
import path from "path";
import { fileURLToPath } from "node:url";
import * as fs from 'fs'


//Start with a function
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const createFolder = () => {
    if(fs.existsSync("capture")){
        return path.join(__dirname, "/capture");
    }else{
        fs.mkdirSync("capture", (err)=>{
            if(err){
                throw (err)
            }
        });
        return path.join(__dirname, "/capture");
    }

}

const init = async () => {
    const browser = await puppeteer.launch({
        headless: "new",
        // headless: false, //puedes ver el browser
        slowMo: 500// poder ver la pagina 
    });
    const page = await browser.newPage();
    await page.goto("https://remoteok.com/");
    //Screen view
    await page.setViewport({
        width: 1920,
        height: 1080
    });
    //Getting time
    await new Promise(r => setTimeout(r, 3000));
    const folder = createFolder();
    await page.screenshot({
        path: `${folder}/page.png` 
    });
    
    await browser.close()
}

init();