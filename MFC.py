from bs4 import BeautifulSoup
import urllib
import re
import csv

fi = open("input.txt", 'r')
fo = open("output.csv", "w+")

fo.write("Manufacturer, MFC Name, Series, Character,  Gender, Scale, Height, Price, 18+?, Cast Off?, Type, Tags, JAN\n")



for i in fi:
	try:
		link = i

		fp = urllib.urlopen(link)

		soup = BeautifulSoup(fp, 'html.parser', from_encoding='utf8')
		fp.close()



		name = soup.title.string.replace(',','|').split(' | ')

		print("Name: " +name[0])
		subNames = name[0].split(' - ')
		print("Origin: " + subNames[0])
		print("Character: " + subNames[-2])
		company = subNames[-1].split('(')
		company = company[-1].split(')')
		print("Companies: " + company[0])
		gender="N"
		print("Scale: "),
		print(company[0])
		fo.write(company[0] + ",")
		fo.write(name[0]+",")
		fo.write(subNames[0]+",")
		fo.write(subNames[-2]+",")
		tags = ""
		scale = ""
		height = ""
		price = ""
		JAN = ""
		for a in soup.find_all('a', class_='item-scale'):
			print(a.contents[0].string + a.contents[1].string),
			scale = a.contents[0].string + a.contents[1].string
		print("")
			
		print("Height: "),
		for aa in soup.find_all('small'):
			if(aa.string=='H='):
				height = aa.next_sibling.string
				print(aa.next_sibling.string),
		print("")
		print("Price: "),
		for b in soup.find_all('span', class_='item-price'):
			price = b.contents[1][1:].replace(",", "")
			print(b.contents[1]),
		print("")
		print("JAN: "),
		for c in soup.find_all('a', title=re.compile('Buy \(?[0-9]+')):
			JAN = c.contents[0]
			print(str(c.contents[0])),
		print('')
		print("Tags: "),
		for d in soup.find_all('div', class_='object-tag'):
			print('\t'+d.a.string)	
			tags = tags+"|"+d.a.string
			if(d.a.string == 'male'):
				gender = "M"
			elif(d.a.string == "female"):
				gender = "F"
		print("")

		print("Gender: " + gender)
		castoff = "N"
		for e in soup.find_all('a'):
			if(e.string == "Castoff"):
				castoff = "Y"
		print("Castoff: " + castoff)
		adult="N"
		for e in soup.find_all('a'):
			if(e.string == "18+"):
				adult="Y"
		print("18+: " + adult)

		fo.write(gender+",")
		fo.write(scale+",")
		fo.write(height+",")
		fo.write(price+",")
		fo.write(adult+",")
		fo.write(castoff+",")
		fo.write(",")
		fo.write(tags+",")
		fo.write(JAN+",")
		fo.write("\n")
	except:
		print("Error on this item: " +i)
		fo.write("Error on this item: " +i)
fo.close()
fi.close()	
