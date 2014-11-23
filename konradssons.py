from bs4 import BeautifulSoup, Tag
import requests
import os, sys
import shutil

headers = {
    'User-agent': 'Mozilla/5.0'
    }

f = open("konradssons.csv", "a")

url = ("http://www.konradssons.com/sortiment/")
r  = requests.get(url,headers=headers)
data = r.text
soup = BeautifulSoup(data)

for i, item  in enumerate(soup.find_all('div', {'class':"javashow"})):
    print "\n"
    print i

    print item
    print item.a['href']


    url = ("http://www.konradssons.com/"+ item.a['href'])
    r  = requests.get(url,headers=headers)

    data = r.text

    child_soup = BeautifulSoup(data)

    series = child_soup.findAll('div', {'class':"serieimages"})

    print series
    for idx,tile in enumerate(series[0].findAll("li")):
        print tile
        print tile.img['src']
        print tile.p.getText()

        manufacturer = "Konradssons"
        name = tile.p.getText()
        image = os.path.basename(tile.img['src'])
        articleno = image.split(".")[0]

        response = requests.get("http://www.konradssons.com"+tile.img['src'], stream=True)
        with open("tiles/" + image.encode('utf-8'), 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

        f.write(name.encode('utf-8') + "," +articleno.encode('utf-8') + "," + manufacturer.encode('utf-8') + "," + image.encode('utf-8')+ "\n")



f.close()
