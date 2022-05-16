
import scrapy


class ProductSpider(scrapy.Spider):
  name = "product"
  start_urls = ["https://www.jumbo.com/producten/bier-en-wijn/bier,-pils/krat/?pageSize=24"]

  def parse(self, response):
    # loop trough all the products on the page and get their information trough css selectors 
    for product in response.css("div.jum-card"): 
      try:
        yield {
          "product-link" : "https://www.jumbo.com/" + "" +  product.css("article div.image-container a").attrib['href'] ,
          "product-name" : product.css("article div.content div.upper div.name h2 a::text").get().strip().replace('\u00a0', ""), 
          "product-price" : product.css("article div.content div.lower div.jum-price div.current-price span.whole::text").get() + "." + product.css("article div.content div.lower div.jum-price div.current-price sup.fractional::text").get()
        }
      except:
        yield {
          # skip the iteration
        }

    # their is a next page button on the page so we are going to itterate through that to get all the products
    offset = 0
    next_page  = response.css("button.jum-button.pagination-button.secondary")[1].attrib['name']
    if next_page is not None and next_page is not 'prev' : 
      offset = offset + 24
      yield response.follow("https://www.jumbo.com/producten/bier-en-wijn/bier,-pils/krat/?offSet="+str(offset)+"&pageSize=24", callback = self.parse)