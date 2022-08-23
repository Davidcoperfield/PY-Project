# Use the request library
import requests
# Set the Target Webpage
url = "http://172.18.58.80/index.php"
r = requests.get(url)

# This will get the status code
print("Status code:")
print(r.status_code)

# This will just get just the headers
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
print(r.text)

# This will modify the headers user-agent
headers = {
    "User-Agent" : "Mobile"
}
url2 = 'http://172.18.58.80/spicyx/'
rh = requests.get(url2, headers=headers)
print(rh.text)

import scrapy

class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.18.58.80/spicyx/']
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

            # To recurse next page
            Page_selector = '.next a ::attr(href)'
            next_page = response.css(Page_selector).extract_first()

            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )