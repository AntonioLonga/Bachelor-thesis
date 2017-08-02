import urllib as url
from bs4 import BeautifulSoup
import re




array_link_github=[]

def getLinkSourceCode(link):

    page=url.request.urlopen(link)
    soup=BeautifulSoup(page,"lxml")

    articleDom=soup.find("article")

    articleStr=str(articleDom)
    
    #print (articleStr)

    for line in articleStr.splitlines():
        
        patternSourceCode="(\<b\>Source Code\</b\>: \<a href=\")([\w\/\:\.\-]*)"
        
        sourceCode=re.match(patternSourceCode,line)
        
        if (sourceCode):
            linkgit= sourceCode.group(2)
            if ("github.com" in linkgit):
                print (linkgit)
                array_link_github.append(linkgit)
                ##nel dubbio li mietto in un file
                with open('linkGiochiGit.txt', 'a') as file:                   
                    file.write(linkgit+","+link)


                
            else:
                print ("##############################################")
                print (linkgit)


                







    

 #elimino il contenuto del file
with open('linkGiochiGit.txt', 'w') as file:
    pass
file.close()



with open("linkGiochi.txt") as infile:
    for link in infile:
        getLinkSourceCode(link)
      

print (len(array_link_github))




