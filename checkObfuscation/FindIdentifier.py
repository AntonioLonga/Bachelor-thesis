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
                #se non li vuoi controllare metti
                # ("\w*.smali")
                
                #cosi controlli anche i file del tipo Qualcosa$qualcosa.smali
                if (re.match("\w*\$?\w*.smali",element)):
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

    #analizza solo il path preso dal attributo package nel manifest.xml
    def start(self,path):
        folder=os.listdir(path)
        pathAnalysis=""



        
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
                self.searchSmaliCode(path+"/smali/"+stringPath)
                

                
        return (self.res)
    ##analizza tutta i smali nella subdirectory smali
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

    #analizza tutte le activity trovate nel manifest
    def start3 (self,path):
        self.res=[]
        setOfPath=set()
        folder=os.listdir(path)

        for element in folder:
            if (element=="AndroidManifest.xml"):
                setOfPath=self.findActivityPath(path+"AndroidManifest.xml")
                       

        for element in setOfPath:
            e=element.replace(".","/")
            if os.path.isfile(path+"smali/"+e+".smali"):
                self.searchInsideFile(path+"smali/"+e+".smali")
        return (self.res)


    def findActivityPath(self,path):
        setOfPath=set()
        with open (path) as manifest:
            for line in manifest:
                #print (line)
                patternPackage="(.*) package=\"([^\s]*)\"(.)*"
                patternActivity="(\s*)<activity (.*)android:name=\"([^\s]*)\"(.*)"
                patternService="(\s*)<service (.*)android:name=\"([^\s]*)\"(.*)"
                patternReceiver="(\s*)<receiver (.*)android:name=\"([^\s]*)\"(.*)"
                activity=re.match(patternActivity, line)
                package=re.match(patternPackage,line)
                service=re.match(patternService,line)
                receiver=re.match(patternReceiver,line)
                if package:
                    pathAnalysis=(package.group(2))
                    setOfPath.add(pathAnalysis)
                if activity:
                    pathAnalysis=activity.group(3)
                    setOfPath.add(pathAnalysis)
                    #print(activity.group(3))
                if service:
                    pathAnalysis=service.group(3)
                    setOfPath.add(pathAnalysis)
                    #psearchSmaliCoderint (pathAnalysis)
              
                if receiver:
                    pathAnalysis=receiver.group(3)
                    setOfPath.add(pathAnalysis)
                    #print (pathAnalysis)
                    
                    

        #print ("lunghezza; "+str(len(setOfPath)))
        #print (setOfPath)
        return (setOfPath)
