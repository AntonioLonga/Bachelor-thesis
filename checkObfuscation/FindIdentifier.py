import sys
import re
import os


class FindIdentifier:
    res=[]

    def __init__(self):
        self.res=[]

    #cerca ricorsivamente all'interno di tutte le catelle e se trova un file.smali
    #chiama il metodo searchInsideFile
    def searchSmaliCode(self,path):
        
        if (os.path.isdir(path)):
            files=os.listdir(path)
            #print("searchSmalicode: ")
            #print (files)

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
        pathAnalysis=""

        #print (folder)


        
        if ("AndroidManifest.xml" in folder):
            with open (path+"AndroidManifest.xml") as manifest:
                for line in manifest:
                    #print (line)
                    patternPackage="(.*) package=\"([^\s]*)\"(.)*"
                    package=re.match(patternPackage,line)
                    if package:
                        pathAnalysis=(package.group(2))

                        
            #verifico che all'interno del percorso ci sia una catella smali e
            #che dentro di lei ci sia la catella com
            #successivamente cerco il pakage

            if not(pathAnalysis==""):

                stringPath=pathAnalysis.replace(".","/")
                #print ("entro")
                print (stringPath)
                self.searchSmaliCode(path+"/smali/"+stringPath)
                

                
        return (self.res)

    def start2(self,path):
        self.res=[]
        folder=os.listdir(path)
               
        for element in folder:
            if (element=="smali"):
                path=path+"/smali"
                subfolder=os.listdir(path)
                for elem in subfolder:
                    self.searchSmaliCode(path+"/"+elem)
            
        return (self.res)
