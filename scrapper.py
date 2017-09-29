from bs4 import BeautifulSoup, url
import pandas
import matplotlib.pyplot as plt
import pymysql
from sqlalchemy import create_engine
import _mysql

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
conn = pymysql.connect(host="127.0.0.1", port=80, user="root", password="", db="test", charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
engine = create_engine('mysql+pymysql://[root]:[]@[127.0.0.1]:[80]/[test]', echo=False)
card_details.to_sql(name="scrap_tb", con=engine, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None)


