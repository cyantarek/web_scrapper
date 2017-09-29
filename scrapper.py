from bs4 import BeautifulSoup, url

page = url("https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38")
soup = BeautifulSoup(page,'lxml')

