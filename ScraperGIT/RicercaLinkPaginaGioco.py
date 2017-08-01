import urllib as url
from bs4 import BeautifulSoup

array_giochi=[]


def getLinkGames(link):
    
    
    page=url.request.urlopen(link)
    
    soup=BeautifulSoup(page,"lxml")
    
    link_giochi=soup.find_all("a",class_="package-header")


    for element in link_giochi:
        gioco=element.get("href")
        gioco=f_droid+gioco
        array_giochi.append(gioco)

    for e in array_giochi:
        print (e)
               

    




f_droid="https://f-droid.org/"
f_droid_browse="https://f-droid.org/packages/"





getLinkGames(f_droid_browse)

for c in range (2,44):
    getLinkGames(f_droid_browse+str(c)+"/")

print (len(array_giochi))


 #elimino il contenuto del file
with open('linkGiochi.txt', 'w') as file:
    pass
file.close()

for element in array_giochi:
    with open('linkGiochi.txt', 'a') as file:                   
        file.write(element+"\n")



file.close()
