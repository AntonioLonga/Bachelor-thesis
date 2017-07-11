from FindIdentifier import FindIdentifier
from AnalysisIdentifier import AnalysisIdentifier
import sys
import argparse
import re
import os


#prendo l'input temporaneamente
#la cartella che contiene la cartella smali....tipo
#../test1/test1.2/


if __name__ == '__main__':
    
    # -------------------------CLI-ARGUMENT-MANAGEMENT-------------------------------- #
    parser = argparse.ArgumentParser (description="Analisi di codice Smali")
    parser.add_argument ('-a', '--apk',  metavar='fileApk', type=str, nargs=1, required=False,
                         help='Specificare il file apk, questo verra disassemblato e poi analizato')
    parser.add_argument ('-d', '--disassembled',  metavar='directory', type=str, nargs=1, required=False,
                         help='Speficicare il file già disassemblato, questo verrà analizato')
    args = parser.parse_args()
    # -------------------------------------------------------------------------------- #

    try:

        if (args.apk):
            print ("hai scelto l'apk: sto disassemblando il file!")
            pathInput=sys.argv[2]
            pathOutput=pathInput[0:-4]

            lancio=("./shell.sh "+pathInput+" "+pathOutput)
            os.system(lancio)

            identifier=FindIdentifier().start(pathOutput)
            AnalysisIdentifier().checkObfuscate(identifier)
        
        if (args.disassembled):
            print ("hai scelto il file disassemblato: sto analizando il file!")
            path=sys.argv[2]            
            identifier=FindIdentifier().start(path)
            AnalysisIdentifier().checkObfuscate(identifier)

                                    
            
    except Exception as e:
        raise (e)







"""
path=sys.argv[1]

identifier=FindIdentifier().start(path)

#print (identifier)

#lengthWord=AnalysisIdentifier.lengthWord(identifier)
#print ("percentuale della parole con lunghezza <=3: "+str(lengthWord))

#repetuteWord=AnalysisIdentifier.percentageRepertuteWord(identifier)
#print ("percentale di parole ripetute: "+str(repetuteWord))


#vowelCount=AnalysisIdentifier.percentageCountVowel(identifier)
#print ("percentale di vocale su tutti i caratteri: "+str(vowelCount))

#average=AnalysisIdentifier.averageWordsLength(identifier)
#print ("lunghezza media delle parole: "+str(average))


#rareBigram=AnalysisIdentifier.countRareBigram(identifier)
#print ("percentuale di bigrammi rari: "+str(rareBigram))


AnalysisIdentifier().checkObfuscate(identifier)
"""
