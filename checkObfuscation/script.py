import sys
import re
import os



def cerca(smalipath):   
    #trova i metodi,calssi,variabile
    patternMetodo=".method (\w*)? (\w*)"
    patternVariabile="(\s*)?(.local )(\w*), \"(\w*)\".*"
    patternClasse=".source \"(\w*).java\""
    print(smalipath)
    with open(smalipath) as infile:
        for line in infile:
            method=re.match(patternMetodo,line)
            variable=re.match(patternVariabile,line)
            classe=re.match(patternClasse,line)
            if method:
                print ("nome del metodo: "+method.group(2))
            if variable:
                print ("nome della variabile: "+variable.group(4))
            if classe:
                print ("nome della classe: "+classe.group(1))





#prendo l'input temporaneamente
#la cartella che contiene lo smali....tipo
#../test1/test1.2/smali/com/example/antonio/myapplication

path=sys.argv[1]
print (path)
smaliFiles=os.listdir(path)



for element in smaliFiles:
    if not(element[0]=="R" and element[1]=="$"):
        if not(element=="R.smali" or element=="BuildConfig.smali"):
            cerca(path+"/"+element)
    





