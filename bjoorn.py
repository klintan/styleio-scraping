from bs4 import BeautifulSoup, Tag
import requests
import os, sys
import shutil

headers = {
    'User-agent': 'Mozilla/5.0'
    }

f = open("bjoorn.csv", "a")

for i in range(0, 300,30):
    print "\n"
    print i
    url = ("http://www.bjoorn.se/shop/shopdet.lasso?skip=%d&cat=Laminate"%i)
    r  = requests.get(url,headers=headers)

    data = r.text

    soup = BeautifulSoup(data)

    # for item in soup.find_all(id="contentinner"):
    #   for sibling in item.next_siblings:
    #       print sibling
    #       if not isinstance(sibling, Tag):
    #           continue
    #       if sibling.name == 'table':
    #           break
    #       print sibling.text
    #   print "-------"

    for idx,item in enumerate(soup.find_all(id="products_container")):
        #print idx
        #print item


        title = item.ul.li.findAll("span", { "class" : "item_heading" })
        print type(title)

        for idx,floor in enumerate(item.findAll("li")):
            #print type(floor)
            #print floor
            manufacturer = floor.findAll("span", { "class" : "item_heading" })[0].getText().split(' ', 1)[0]
            name =  floor.findAll("span", { "class" : "item_heading" })[0].getText().split(' ', 1)[1]
            #print floor.findAll("span", { "class" : "item_heading" })[0]

            #print floor.findAll("div", { "class" : "product_logo_overlay" })[0].img['src']
            #print floor.findAll("img", { "class" : "productPicSmall" })[0]['src']
            image = "http://www.bjoorn.se/"+floor.findAll("img", { "class" : "productPicSmall" })[0]['src']

            print manufacturer
            print name
            print os.path.basename(image)



            #floor.getText()
            #response = requests.get(image, stream=True)
            #with open('floors/' + os.path.basename(image).encode('utf-8'), 'wb') as out_file:
             #        shutil.copyfileobj(response.raw, out_file)
            #del response
            #print idx
        # for idy,floors in enumerate(item.table):
        #     #for wallpaper in wallpapers.td:
        #     print idy
        #     for x in range(0,4):
        #     #print wallpaper.contents
        #     #print wallpaper.next_sibling
        #     #print wallpaper
        #     #print wallpaper
        #         prodThumb
        #         link = floors.contents[x].a.get('href')
        #         name = floors.contents[x].p.getText()
        #         articleno = floors.contents[x].p.next_sibling.getText()
        #         manufacturer = floors.contents[x].p.next_sibling.next_sibling.getText()
        #         image = floors.contents[x].a.img.get('src')
        #         image = image.replace("smallpics","closepics")
        #         print image

            response = requests.get(image, stream=True)
            with open(os.path.basename(image).encode('utf-8'), 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
        #     #soup1 = BeautifulSoup(wallpaper)
        #     #print soup1
        #     #link = soup1.a.get('href')
        #     # link = item.table.td.a.get('href')
        #     # name = item.table.td.p.getText()
        #     # articleno = item.table.td.p.next_sibling.getText()
        #     # manufacturer = item.table.td.p.next_sibling.next_sibling.getText()
        #     # #print name
        #     # #print articleno
        #     # #print manufacturer
        #     # image = item.table.td.a.img.get('src')
        #     # #print str.replace("is", "was");
        #     # image = image.replace("smallpics","closepics")
        #     # #print os.path.basename(image)
        #     # #print image
            articleno = ''
            floortype = 'laminate'

            f.write(name.encode('utf-8') + "," +articleno.encode('utf-8') + "," + manufacturer.encode('utf-8') + "," + os.path.basename(image).encode('utf-8')+ ","  + floortype.encode('utf-8') +"\n")

            #url1 = ("http://www.tapetorama.se/"+link)
            #r1  = requests.get(url,headers=headers)
            #data1 = r1.text

            #soup1 = BeautifulSoup(data1)


    #for td in soup.find_all('table'):
    #   print ""
        #print td.find_all('tbody')
f.close()