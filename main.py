import asyncio

import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent



BASE_URL = "https://auto.kufar.by/l/cars/bez-posrednikov?cnd=1&cur=BYR"
HEADERS = {"User-Agent": UserAgent().random}

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers = HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, "html.parser")

            items = soup.find_all("a", {"class": "styles_wrapper__X1uDr"})
            file_1 = open("file.txt", "a", encoding='utf-8')
            
            for item in items:
                
                title = item.find("h3", {"class": "styles_title__fPBW6 styles_ellipsis__pGA5h"}).text.strip()
                info = item.find("p", {"class": "styles_params__KP_ho styles_ellipsis__pGA5h"}).text.strip()
                yer = item.find("div", {"class": "styles_year__Z7IqC"}).text.strip()
                mileage = item.find("div", {"class": "styles_mileage__tJK9M"}).text.strip()
                price = item.find("div", {"class": "styles_price__1e9XN"}).text.strip()
                city = item.find("div", {"class": "styles_bottom__region___ar0u"}).text.strip()
                link = item.get('href')
                


                res =  link[:link.find('?')]
                
                file_1.write(res+"\n")
            
                
                print(f"New Title: {title, info, yer, mileage, price, city, link[:link.find('?')]}")

                

        
    

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())