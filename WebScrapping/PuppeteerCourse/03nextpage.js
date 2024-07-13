import puppeteer from "puppeteer";
import ExcelJs from "exceljs";


const init = async () => {
    const browser = await puppeteer.launch({
        headless: false,
        defaultViewport: false
    });
    const page = await browser.newPage();
    await page.setViewport({
        width: 1920,
        height: 1080
    });
    await page.goto("https://listado.mercadolibre.com.ve/baterias-percusion-accesorios-platillos/platillos_Desde_97_NoIndex_True",{waitUntil: "load"});

    const is_disable = await page.$("li.andes-pagination__button.andes-pagination__button--next > a") !== null;

    console.log(is_disable);
    page.click("li.andes-pagination__button.andes-pagination__button--next > a");

    

    // await browser.close();

};

// init();
const saveExcel = (data)=> {
    
    const workbook = new ExcelJs.Workbook();
    //File name
    const excel_Filename = "productos.xlsx";

    //Sheet
    const sheet = workbook.addWorksheet("results");

    const reColumns = [
        {header: "Img", key: "img"},
        {header: "Title", key: "title"},
        {header: "Price", key: "price"},
        {header: "Link", key: "link"}
    ];

    sheet.columns = reColumns;
    data.forEach(element => {
        sheet.addRow(element)
    });
    
    workbook.xlsx.writeFile(excel_Filename)
        .then((e)=>{
            console.log("File was created");
        }).catch(()=>{
            console.log("Something went wrong");
        })
 
}

const init2 = async () => {
    const browser = await puppeteer.launch({
        headless: "new",
        defaultViewport: false,
        userDataDir: "./tmp"
    });

    const page = await browser.newPage();
    await page.setViewport({
        width: 1920,
        height: 1080
    });
    // const url = "https://listado.mercadolibre.com.ve/laptops#D[A:laptops]";
    // const url = "https://listado.mercadolibre.com.ve/platillos#D[A:platillos]";
    const url = "https://listado.mercadolibre.com.ve/gorras#D[A:gorras]";
    await page.goto(url,{ waitUntil: "load",timeout: 0});

    
    let isBtnDisabled = false;
    let productList = [];
    while (!isBtnDisabled) {
        await page.waitForSelector(".ui-search-results")
        //Container
        const container = await page.$$(".ui-search-layout__item");
        //Loop all handles 
        for (const items of container){
            let img = "Null";
            let title = "Null";
            let price = "Null";
            let link = "Null";
            let TitleArray = [];
        
            try {
            
                img = await page.evaluate(el => el.querySelector(".ui-search-result-image__element").getAttribute("src"), items)

            } catch (error) {
                console.log("Error Img:"+ " ",error.message);
            }

            try {
                //Title
                title = await page.evaluate(el => el.querySelector(".ui-search-item__title").textContent, items)

                TitleArray.push(title)
             

            } catch (error) {
                console.log("Error Title:"+ " ",error.message);
            }

            try {
                //Price
                price = await page.evaluate(el => el.querySelector(".andes-money-amount__fraction").textContent, items)
 
            } catch (error) {
                console.log("Error Price:"+ " ",error.message);
            
            }

            try{
                //link
                link = await page.evaluate(link => link.querySelector(".ui-search-link").getAttribute("href"),items)

            }catch (error){
                console.log("Error link:"+ " ",error.message);
            }

            const product = {
                img: img,
                title: title,
                price: price,
                link: link 
            }

            productList.push(product);
            
        }

        const exits = await page.$(".andes-pagination__button--next") !== null;
        

        if(exits){
            await page.waitForSelector("li.andes-pagination__button.andes-pagination__button--next > a", {visible: true})
            await page.click("li.andes-pagination__button.andes-pagination__button--next > a");
        }

        if(!exits){
            isBtnDisabled = true;
        }
    }
   
    console.log(productList.length + 1);
    await browser.close();

    saveExcel(productList);

}

init2()