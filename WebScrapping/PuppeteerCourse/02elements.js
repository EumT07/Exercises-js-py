import puppeteer from "puppeteer";


//Start with a function

const init = async () => {
    const browser = await puppeteer.launch({
        headless: "new",
        slowMo: 500,
        defaultViewport: false,
        userDataDir: "./tmp"
    });
    const page = await browser.newPage();
    
    await page.goto("https://listado.mercadolibre.com.ve/samsung-a13#D[A:samsung%20a13]", 
    { waitUntil: "load",
    timeout: 0}
    );
  

    //VA esperar hasta tener el selector
    await page.waitForSelector(".ui-search-results");

    const productsList = await page.$$(".ui-search-layout__item");
    
    for (const element of productsList ) {

        try {
            const title = await element.$(".ui-search-item__title");
            const imglink = await element.$(".ui-search-result-image__element");
            const tienda = await element.$(".ui-search-official-store-label");
            const price = await element.$(".andes-money-amount__fraction");

            //Result
            const getTitle = await page.evaluate(title => title.innerHTML, title);
            const getPrice = await page.evaluate(price => price.innerHTML, price);
            let getImg = await page.evaluate(imglink => imglink.getAttribute("src"), imglink);
            
            let getTienda = null;

            if(tienda == null){
                getTienda = "No Store Name"
            }else{
                getTienda = await page.evaluate(tienda => tienda.innerHTML, tienda);
            }
            
            const data = {
                "Page": "Mercado Libre",
                productTitle: getTitle,
                productImg: getImg,
                productTienda: getTienda,
                productPrice: getPrice
            }
        
            console.log(data);

        } catch (error) {
            console.log("Error --> ", error);
        }
    }

    // await new Promise(r => setTimeout(r, 3000));
    // await browser.close()
}

// init();


const init2 = async () => {
    const browser = await puppeteer.launch({
        headless: "new",
        defaultViewport: false,
        userDataDir: "./tmp"
    });

    const page = await browser.newPage();
    // const url = "https://computacion.mercadolibre.com.ve/conectividad-redes-routers-access-points/tp-link/access-point_NoIndex_True#applied_filter_id%3DBRAND%26applied_filter_name%3DMarca%26applied_filter_order%3D2%26applied_value_id%3D7885%26applied_value_name%3DTP-Link%26applied_value_order%3D45%26applied_value_results%3D1178%26is_custom%3Dfalse"
    const url = "https://listado.mercadolibre.com.ve/laptops#D[A:laptops]";
    await page.goto(url,{ waitUntil: "load",timeout: 0});

    //Container
    const container = await page.$$(".ui-search-layout__item")

    //Loop all handles 
    for (const items of container){
        let img = "Null";
        let link = "Null";
        // let title = "Null";
        // let price = "Null";
        // let raiting = "Null";
        // let raiting_value = "Null"
        // let TitleArray = [];
        

        try {
            
            img = await page.evaluate(el => el.querySelector(".ui-search-result-image__element").getAttribute("src"), items)

        } catch (error) {
            console.log(error.message);
        }

        try{
            //link
            link = await page.evaluate(link => link.querySelector(".ui-search-link").getAttribute("href"),items)

        }catch (error){
            console.log("link ",error.message);

        }
        // try {
        //      //Title
        //      title = await page.evaluate(el => el.querySelector(".ui-search-item__title").textContent, items)

        //      TitleArray.push(title)
             

        // } catch (error) {
        //     console.log(error.message);
        // }

        // try {
        //     //Price
        //     price = await page.evaluate(el => el.querySelector(".andes-money-amount__fraction").textContent, items)
 
        // } catch (error) {
        //     console.log(error.message);
            
        // }

        // try {
        //     //Raiting
        //     raiting = await items.$(".ui-search-reviews__rating-number");
        //     raiting_value = await page.evaluate(el => el.textContent, raiting);
        // } catch (error) {
        //     console.log(error.message);
            
        // }

        
        // let titleFilter = TitleArray.filter((el) => el.toLowerCase().includes("outdoor"))
        // console.log(`Product: \n Title: ${titleFilter}}`);
        // console.log(`Products:\n Img: '${img}'\n Title: '${titleFilter}'\n Price: '$ ${price}'\nRaiting: '${raiting_value} of 5' `);

        console.log(`Products:\n Img: '${img}\n link: ${link}'`);
    }
}

init2()