from bs4 import BeautifulSoup, url

page = url("http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
soup = BeautifulSoup(page,'lxml')
all_data = soup.find_all("div", {"class":"propertyRow"})
price = all_data[0].find("h4", {"class":"propertyPrice"})
print(all_data)

