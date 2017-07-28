from FindIdentifier import FindIdentifier
from AnalysisIdentifier import AnalysisIdentifier
import sys
import argparse
import os


if __name__ == '__main__':
    
    # -------------------------CLI-ARGUMENT-MANAGEMENT-------------------------------- #
    parser = argparse.ArgumentParser (description="Analisi di codice Smali")
    parser.add_argument ('-a', '--apk',  metavar='fileApk', type=str, nargs=1, required=False,
                         help='Specificare il file apk, questo verra disassemblato e poi analizato')
    parser.add_argument ('-d', '--disassembled',  metavar='disassembled', type=str, nargs=1, required=False,
                         help='Speficicare il file già disassemblato, questo verrà analizato')
    parser.add_argument ('-di', '--directory', metavar='directory', nargs=1, required=False,
                         help='Specificare folder contenenti app disassemb. e crea un file result')
    args = parser.parse_args()
    # -------------------------------------------------------------------------------- #

    try:

        if (args.apk):
            print ("hai scelto l'apk: sto disassemblando il file!")
            pathInput=sys.argv[2]
            pathOutput=pathInput[0:-4]

            lancio=("./shell.sh "+pathInput+" "+pathOutput)
            os.system(lancio)
            identifier=FindIdentifier().start(pathOutput+"/")
            string=AnalysisIdentifier().checkObfuscate(identifier)
            identifier2=FindIdentifier().start2(pathOutput+"/")
            string2=AnalysisIdentifier().checkObfuscate(identifier2)
            
            identifier3=FindIdentifier().start3(pathOutput+"/")
            string3=AnalysisIdentifier().checkObfuscate(identifier3)
            tot =string+string2+string3
            bol="error"
            if (tot<2.09474):
                bol=False
            elif (tot>2.68118):
                bol=True
            else:
                bol=None
            print (str(tot)+"\t\t\t"+str(bol))
            
        
        if (args.disassembled):
            print ("hai scelto il file disassemblato: sto analizando il file!")          
            path=sys.argv[2]
            
            #aggiungo / se non è stato inserito
            if not(path[-1]=="/"):
                path=path+"/"

                
            identifier=FindIdentifier().start(path)
            string=AnalysisIdentifier().checkObfuscate(identifier)
            identifier2=FindIdentifier().start2(path)
            string2=AnalysisIdentifier().checkObfuscate(identifier2)

            identifier3=FindIdentifier().start3(path)
            string3=AnalysisIdentifier().checkObfuscate(identifier3)

                     
            tot =string+string2+string3
            bol="error"
            if (tot<2.09474):
                bol=False
            elif (tot>2.68118):
                bol=True
            else:
                bol=None
            print (str(tot)+"\t\t\t"+str(bol))
            
            
        if (args.directory):
            print ("hai scelto un dir contennte + app disassemblate")
            path=sys.argv[2]

            #aggiungo / se non è stato inserito
            if not(path[-1]=="/"):
                path=path+"/"
                
            folder= os.listdir(path)
            
            #elimino il contenuto del file
            with open('result.csv', 'w') as file:
                pass
            file.close()
            
            for element in folder:
                
                
                if not(element=="apk"):
                
                    find=FindIdentifier()
                    identifier=[]
                    identifier1=find.start(path+"/"+element+"/")
                    string=AnalysisIdentifier().checkObfuscate(identifier1)

                    identifier2=find.start2(path+"/"+element+"/")
                    string2=AnalysisIdentifier().checkObfuscate(identifier2)
                    identifier3=find.start3(path+"/"+element+"/")
                    string3=AnalysisIdentifier().checkObfuscate(identifier3)
                    tot=(string+string2+string3)
                    bol="error"
                    if (tot<2.09474):
                        bol=False
                    elif (tot>2.68118):
                        bol=True
                    else:
                        bol=None
                    print (element+"\t\t\t"+str(tot)+"\t\t\t"+str(bol))
                    #scrivo nel file i risultatit
                    with open('result.csv', 'a') as file:
                        #qui stampo solo il totale
                        #file.write(element+","+(str(string+string2+string3))+"\n")

                        #qui li stampo singolarmente per analizarli
                        
                        file.write(element+","+(str(string))+","+(str(string2))+","+(str(string3))+","+str(tot)+","+str(bol)+"\n")
                                    
            file.close()
    except Exception as e:
        raise (e)
            

