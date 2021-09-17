from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?d=graphic+card'

# open connection, grab the contents of the url, close
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

#inspected from the web page
page_soup.body.iframe # <iframe> inside <body> html tag

# grab the containers of the products
containers = page_soup.findAll("div", {"class":"item-container"})

container = containers[0]   

title_container = container.findAll("a", {"class":"item-title"})

print(title_container[0].text)