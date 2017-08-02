import urllib as url
from bs4 import BeautifulSoup
import re



def checkObfuscate(html):


    soup=BeautifulSoup(html,"lxml")

    testo=soup.text
    pattern="(\s*)buildTypes {(\s*)"
    bool=False

    textAfterBuild=""

    for t in testo.splitlines():
        if bool and t != "":
            textAfterBuild=textAfterBuild+t+"\n"
        if re.match(pattern,t):
            bool=True
   



    buildTypes=""
    count=1
    for t in textAfterBuild:
        if (count>0):
            if t=="{":
                count=count+1
            if t=="}":
                count=count-1

        if (count>0):
            buildTypes=buildTypes+t
   



    patternRelease="(\s*)release {(\s*)"
    b=False

    textAfterRelease=""

    for t in buildTypes.splitlines():
        if b and t!="":
            textAfterRelease=textAfterRelease+t+"\n"
        if re.match(patternRelease,t):
            b=True



    patternEnable="(\s*)minifyEnabled (\w*)"
    for t in textAfterRelease.splitlines():
        if (re.match(patternEnable,t)):
            ris=re.match(patternEnable,t)
            risultato=ris.group(2)
            if risultato=="true":
                return True
            else:
                return False
    
    



html=""

with open ("tmp.html") as file:
    for line in file:
        html=html+line

print (checkObfuscate(html))
