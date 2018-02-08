import urllib.request
from bs4 import BeautifulSoup

#page url
url = "http://univ.cc/search.php?dom=world&key=&start="

#last page count
last = 7501

#text file
pt = open("universities.txt", "w")


#function to read 
def readpage(pageLink,pageCount):
 links = []
 try:
     resp = urllib.request.urlopen(pageLink+str(pageCount))
     soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
     for link in soup.find("ol", {"start":pageCount}).find_all('a', href=True):
         links.append(str(link.get_text())+','+link['href'])
 except:
 	pass
 return links


for i in range(1,last,50):
	links = []
	links = readpage(url,i)
	percent = int((i/last)*100)
	percent_left = int(((last-i)/last)*100)
	print(str(percent)+"% done "+str(percent_left)+"% left")
	for i in links:
		try:
			pt.write(i+"\n")
		except:
			pass

pt.close



