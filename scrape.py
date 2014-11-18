from bs4 import BeautifulSoup, Tag
import requests
import os, sys
import shutil

headers = {
    'User-agent': 'Mozilla/5.0'
    }

f = open("wallpapers.csv", "a")

for i in range(362, 362):
	print "\n"
	print i
	url = ("http://www.tapetorama.se/list.php?PrintYear=&Manufacturer=&BGColor=&Pattern=&Texture=&Amount=&Sort=&pagecounter=%d&Searchtype=Advanced&category=Wallpaper" %i)
	r  = requests.get(url,headers=headers)

	data = r.text

	soup = BeautifulSoup(data)

	# for item in soup.find_all(id="contentinner"):
	# 	for sibling in item.next_siblings:
	# 		print sibling
	# 		if not isinstance(sibling, Tag):
	# 			continue
	# 		if sibling.name == 'table':
	# 			break
	# 		print sibling.text
	# 	print "-------"

	for idx,item in enumerate(soup.find_all(id="contentinner")):
		#print idx
		for idy,wallpaper in enumerate(item.table):
			#for wallpaper in wallpapers.td:
			print idy
			for x in range(0,4):
			#print wallpaper.contents
			#print wallpaper.next_sibling
			#print wallpaper
			#print wallpaper
				#link = wallpaper.contents[x].a.get('href')
				#name = wallpaper.contents[x].p.getText()
				#articleno = wallpaper.contents[x].p.next_sibling.getText()
				#manufacturer = wallpaper.contents[x].p.next_sibling.next_sibling.getText()
				image = wallpaper.contents[x].a.img.get('src')
				image = image.replace("smallpics","closepics")
				print image

				response = requests.get(image, stream=True)
				with open(os.path.basename(image).encode('utf-8'), 'wb') as out_file:
					shutil.copyfileobj(response.raw, out_file)
				del response
			#soup1 = BeautifulSoup(wallpaper)
			#print soup1
			#link = soup1.a.get('href')
			# link = item.table.td.a.get('href')
			# name = item.table.td.p.getText()
			# articleno = item.table.td.p.next_sibling.getText()
			# manufacturer = item.table.td.p.next_sibling.next_sibling.getText()
			# #print name
			# #print articleno
			# #print manufacturer
			# image = item.table.td.a.img.get('src')
			# #print str.replace("is", "was");
			# image = image.replace("smallpics","closepics")
			# #print os.path.basename(image)
			# #print image

				#f.write(name.encode('utf-8') + "," +articleno.encode('utf-8') + "," + manufacturer.encode('utf-8') + "," + os.path.basename(image).encode('utf-8')+"\n")

			#url1 = ("http://www.tapetorama.se/"+link)
			#r1  = requests.get(url,headers=headers)
			#data1 = r1.text

			#soup1 = BeautifulSoup(data1)


	#for td in soup.find_all('table'):
	#	print ""
   		#print td.find_all('tbody')
f.close()