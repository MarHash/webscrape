from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.bbc.com/news'

# open connection, grab the contents of the url, close
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"gs-c-promo nw-c-promo gs-o-faux-block-link gs-u-pb gs-u-pb+@m nw-p-default gs-c-promo--inline gs-c-promo--"
	"stacked@m nw-u-w-auto gs-c-promo--flex"})

container = containers[0].div

print(container.findAll("div", {"class":"gs-o-media-island"})[0].div)