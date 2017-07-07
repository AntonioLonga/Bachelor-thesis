import sys
import re
import os


class FindIdentifier:
    res=[]

    #cerca ricorsivamente all'interno di tutte le catelle e se trova un file.smali
    #chiama il metodo searchInsideFile
    def searchSmaliCode(self,path):
        
        if (os.path.isdir(path)):
            files=os.listdir(path)

            for element in files:
                if (re.match("\w*.smali",element)):
                    #print ("smali: "+element)
                    self.searchInsideFile(path+"/"+element)
                else:
                    self.searchSmaliCode(path+"/"+element)



    
    def searchInsideFile(self,smalipath):
        """Return name of variables, calsses and method.
        This method take as input the path of smali file, and return an array of names
        """
        #trova i metodi,calssi,variabile
        patternMetodo=".method (\w*)? (\w*)"
        patternVariabile="(\s*)?(.local )(\w*), \"(\w*)\".*"
        patternClasse=".source \"(\w*).java\""

        
        with open(smalipath) as infile:
            for line in infile:
                notIdentifier={"constructor","static","abstract","final"}
                method=re.match(patternMetodo,line)
                variable=re.match(patternVariabile,line)
                classe=re.match(patternClasse,line)
                if (method and not(method.group(2) in (notIdentifier))):
                    #print ("nome del metodo: "+method.group(2))
                    self.res.append(method.group(2))
                if variable:
                    #print ("nome della variabile: "+variable.group(4))
                    self.res.append(variable.group(4))
                if classe:
                    #print ("nome della classe: "+classe.group(1))
                    self.res.append(classe.group(1))
    def start(self,path):
        folder=os.listdir(path)

        
        #verifico che all'interno del percorso ci sia una catella smali e
        #che dentro di lei ci sia la catella com

        for element in folder:
            if (element=="smali"):
                path=path+"/smali"
                subfolder=os.listdir(path)
                for elem in subfolder:
                    if (elem=="com"):
                       self.searchSmaliCode(path+"/com")


        return (self.res)
