from bs4 import BeautifulSoup, url

page = url("https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38")
soup = BeautifulSoup(page,'lxml')

cards = soup.find_all("div", {"class":"item-container"})

for card in cards:
    card_brand = card.div.div.a.img["title"]
    card_name = card.find_all("a", {"class":"item-title"})[0].text
    shipping = card.find_all("li", {"class":"price-ship"})[0].text.replace(" ", "").strip()

    print(shipping)

