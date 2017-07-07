from FindIdentifier import FindIdentifier
from AnalysisIdentifier import AnalysisIdentifier
import sys
import re
import os


#prendo l'input temporaneamente
#la cartella che contiene la cartella smali....tipo
#../test1/test1.2/


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
