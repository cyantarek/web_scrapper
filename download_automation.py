from urllib import request

with open("text_download.txt", "wb") as f:
    page = request.urlopen("https://automatetheboringstuff.com/files/rj.txt")
    f.write(page.read())
