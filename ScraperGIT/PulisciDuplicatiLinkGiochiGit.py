import urllib as url
from bs4 import BeautifulSoup

elementi=set()
ris=""
with open("linkGiochiGit.txt") as infile:
    
    for link in infile:
        elementi.add(str(link))






        

 #elimino il contenuto del file
with open('linkGiochiGitNODUPLICATI.txt', 'w') as file:
    pass
file.close()



with open('linkGiochiGitNODUPLICATI.txt', 'a') as file:                   
    for a in elementi:
        file.write(a)


print (len(elementi))
                
