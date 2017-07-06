import sys
import re
import os

res=[]

#cerca ricorsivamente all'interno di tutte le catelle e se trova un file.smali
#chiama il metodo searchInsideFile
def searchSmaliCode(path):

    if (os.path.isdir(path)):
        files=os.listdir(path)

        for element in files:
            if (re.match("\w*.smali",element)):
                print ("smali: "+element)
                searchInsideFile(path+"/"+element)
            else:
                searchSmaliCode(path+"/"+element)



    
def searchInsideFile(smalipath):
    """Return name of variables, calsses and method.
    This method take as input the path of smali file, and return an array of names
    """
    #trova i metodi,calssi,variabile
    patternMetodo=".method (\w*)? (\w*)"
    patternVariabile="(\s*)?(.local )(\w*), \"(\w*)\".*"
    patternClasse=".source \"(\w*).java\""

    
    with open(smalipath) as infile:
        for line in infile:
            method=re.match(patternMetodo,line)
            variable=re.match(patternVariabile,line)
            classe=re.match(patternClasse,line)
            if (method and not(method.group(2)=="constructor" or method.group(2)=="static" or method.group(2)=="abstract" or method.group(2)=="final")):
                print ("nome del metodo: "+method.group(2))
                res.append(method.group(2))
            if variable:
                print ("nome della variabile: "+variable.group(4))
                res.append(variable.group(4))
            if classe:
                print ("nome della classe: "+classe.group(1))
                res.append(classe.group(1))




#prendo l'input temporaneamente
#la cartella che contiene la cartella smali....tipo
#../test1/test1.2/


path=sys.argv[1]
folder=os.listdir(path)

#verifico che all'interno del percorso ci sia una catella smali e
#che dentro di lei ci sia la catella com

for element in folder:
    if (element=="smali"):
        path=path+"/smali"
        subfolder=os.listdir(path)
        for elem in subfolder:
            if (elem=="com"):
                searchSmaliCode(path+"/com")


print(res)

    










"""
for element in smaliFiles:
    if not(element[0]=="R" and element[1]=="$"):
        if not(element=="R.smali" or element=="BuildConfig.smali"):
            searchInsideFile(path+"/"+element)
 """ 





