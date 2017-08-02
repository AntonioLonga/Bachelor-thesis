import urllib as url
from bs4 import BeautifulSoup



import requests



def getGradleFile(link):


    ret = requests.head(link)
    print(ret.status_code)

    if (ret.status_code<400):


       
        pageGioco=url.request.urlopen(link)
    
        soupGioco=BeautifulSoup(pageGioco,"lxml")
    
        elements=soupGioco.find_all("a",class_="js-navigation-open")

        for element in elements:
            title=element.get("title")
            if(title=="app"):
                linkapp=element.get("href")
                linkapp="https://github.com"+linkapp

            
                pageApp=url.request.urlopen(linkapp)
                soupApp=BeautifulSoup(pageApp,"lxml")
                files=soupApp.find_all("a",class_="js-navigation-open")

                for file in files:
                    titolo=file.get("title")
                    if (titolo=="build.gradle"):
                        linkBuild=file.get("href")
                        linkBuild="https://github.com"+linkBuild
                        print (linkBuild)
                        return linkBuild

    else:
        print ("non va: "+link)
        return None
                







 #elimino il contenuto del file
with open('linkAppGitBuild.txt', 'w') as file:
    pass
file.close()

#linkGiochiGitNODUPLICATI


with open("linkGiochiGitNODUPLICATI.txt")as infile:
    for line in infile:
        element=line.split(",")
        linkgit= element[0]

        linkBuild=getGradleFile(linkgit)
        if not(linkBuild==None):
            with open('linkAppGitBuild.txt','a') as file:
                file.write(element[0]+","+linkBuild+","+element[1])
