from bs4 import BeautifulSoup, url
import csv
import pandas
import matplotlib.pyplot as plt

page = url("https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38")
soup = BeautifulSoup(page, 'lxml')

cards = soup.find_all("div", {"class": "item-container"})
card_name = [name.text for name in soup.find_all("a", {"class": "item-title"})]
card_brand = [name.text.split()[0] for name in soup.find_all("a", {"class": "item-title"})]
shipping = [ship.text.strip() for ship in soup.find_all("li", {"class": "price-ship"})]


print(shipping)

print(card_brand)
card_details = pandas.DataFrame({
    "Name": card_name,
    "Brand": card_brand,
    "Shipping": shipping
})
card_details.to_csv("output.csv")

card_details.plot(kind="line")
plt.show()
