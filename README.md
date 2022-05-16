# Jumbo-bier-scraper
This is a python scraper for a specific part of a site. I had never worked with python before so I did this just to practice. 

I used a scraper framework called Scrapy for python. It was really easy to use and if I ever need to make a scraper with python again I would use it again. 

All this scraper does is scraping all crates of beer. 

It retrieves the following: 
- name of product
- price of product (original price)
- link to the product page

if you want to run the scraper you can run it with the following command (assuming you have all the necessary dependencies needed)

scrapy crawl product -O product.json

this command will scrape everything and create a new file called product.json
all the items scraped will be stored inside that json file




