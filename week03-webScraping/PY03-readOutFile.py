from bs4 import BeautifulSoup
with open("/Users/cobhanphillipson/Desktop/GMIT/2019-2/Data-Representation/carviewer.html") as fp:
 soup = BeautifulSoup(fp,'html.parser')
print (soup.tr)
#print (soup.tr)
rows = soup.findAll("tr")
for row in rows:
 #print(row)
 cols = row.findAll("td")
 dataList = []
 for col in cols:
    dataList.append(col.text)
    print (dataList)
    