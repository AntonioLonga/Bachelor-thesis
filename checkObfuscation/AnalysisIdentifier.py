import re

rareBigram=set()

class AnalysisIdentifier:


    
    def checkObfuscate(self,input):
        #contiene la lunghezza totatle delle parole
        totalLengthWordsOnArray=0
        wordDict=dict()
        for element in input:
            totalLengthWordsOnArray=totalLengthWordsOnArray+len(element)
            if (element in wordDict):
                wordDict[element]=wordDict[element]+1
            else:
                wordDict[element]=1
      
            
            

        

        #se l'nput che passo è vuoto, sighifica che il path nel manifest  non porta a nessuna cartella, quindi sicuramente offuscato
        if input==[]:
            return 1
        
        #contiene la % di parole con lung minore uguale a 3
        lengthWord=self.lengthWord(input)
        #contiene la % di parole ripetute
        repetuteWord=self.percentageRepetuteWord(input,wordDict)
        #contiene la % di parole che hanno meno del 25% di vocali
        countVowel=self.percentageCountVowel(input)
        #contiene la lungheza media delle parole
        percenageLength=self.percenageWordsLength(input,totalLengthWordsOnArray)
        #contiene la % di bigrammi rari
        rareBigram=self.percentageRareBigram(input)
        #print ("% di parole con lung. <= a 3: "+str(lengthWord))
        #print ("% di identificatori ripetuti: "+str(repetuteWord))
        #print ("% parole con meno del 25% di vocali: "+str(countVowel))
        #print ("% di parole con lung. <= a 9: "+str(percenageLength))
        #print ("% di bigrammi rari: "+str(rareBigram))


        #range identificatori piu corti di 3 caratteri
        
       # print (self.average(0.93,25.72,lengthWord))
       # print (self.average(15.45,50.35,repetuteWord))
       # print (self.average(20.8,33.75,countVowel))
       # print (self.average(15.43,50.35,percenageLength))
       # print (self.average(0.28,5.65,rareBigram))
        
        length=(self.average(0.93,25.72,lengthWord))
        repetute= (self.average(15.45,50.35,repetuteWord))
        vocali= (self.average(20.8,33.75,countVowel))
        #percLength= (self.average(15.43,50.35,percenageLength))
        bigram=(self.average(0.28,5.65,rareBigram))
        percLength=0
        if percenageLength<= 9:
            percLength=1
        else:
            percLength=0

        


        
        identifier1=(length+repetute+vocali+percLength+bigram)/5
        #print ("Indicatore di offuscamento con media pesata")
        #print(identifier1)
        
        #identifier2=(self.average2(length,repetute,vocali,percLength,bigram))
        #print ("Indicatore di offuscamento con metodo 2")
        #print (identifier2)

        #return (str(identifier1)+"\t\t"+str(identifier2))
        return (identifier1)
        

   
    """Return percentage of words that have length less or equals than 3 characters
    This method take an array of words as input, and return percenage of word that
    have length less or equals than tresholder, the tresholder is set on 3"""     
    def lengthWord(self,input):
        if (input==[] or input==None):
            print ("qualcosa non va nel metodo:")
            print ("AnalysisIdentifier().lenghtWord()")
            return 0
        
            
        percentage=0;
        inputLength=len(input)
        lessTresholder=0
        for element in input:
            if len(element) <= 3 :
                lessTresholder=lessTresholder+1
        if inputLength==0:
            percentage= 0
        else:
            percentage= (100*lessTresholder)/inputLength
            percentage = float("{0:.2f}".format(percentage))
        return (percentage)

    def average(self,lower,upper, value):
        result= (value-lower)/(upper-lower)
        return result;

    def average2(self,leng,rep,vow,percLen,big):
        value=0
        if (leng<=0.93):
            value=value-1
        elif (leng>=25.72):
            value=value+1

        if (rep<=15.45):
            value=value-1
        elif(rep>=50.35):
            value=value+1

        if (vow>=30.75):
            value=value-1
        elif (vow<=20.8):
            value=value+1

        if (percLen<=15.45):
            value=value-1
        elif (percLen>=50.35):
            value=value+1

        if (big<=0.28):
            value=value-1
        elif (big>=5.65):
            value=value+1


        value= (value+5)/10
        return (value)
            
            
            ###ÀÀÀÀÀÀÀÀÀÀ#### INIZIO REFACRING
            # PER INTERROGARE DA SHELL
            # from AnalysisIdentifier import AnalysisIdentifier as A
            # A().metodo(parametro)
    
    """Return percentage of repetute words 
    This method take an array of words as input, and return percenage of repetute word  
    """   
    def percentageRepetuteWord(self,input,wordDict):
    
        #wordSet=set()
        #wordSet2=set()

        

        
        ripetute=0
        for x in wordDict:
            if wordDict[x] >1:
                ripetute=ripetute+wordDict[x]
                
        if len(input)==0:
            percentage=0
        else: 
            percentage=(100*ripetute)/len(input)
        
        return percentage

    

    """Return precentage of words that has vowel less than 25% 
    """
    def percentageCountVowel(self,input):
        vowels= {"a","e","i","o","u"}
        vowelsCount=0
        #totalCharacter=0
        totalWord=0
        for word in input:
            wordChar=0
            wordVowel=0
            totalWord=totalWord+1
            for char in word:
                wordChar=wordChar+1
                if char in vowels:
                    wordVowel=wordVowel+1
            if wordChar==0:
                tempPercentage=0
            else:
                tempPercentage=(100*wordVowel)/wordChar
            if tempPercentage<25:
                vowelsCount=vowelsCount+1
        if totalWord==0:
            percentage=0
        else:
            percentage=(100*vowelsCount)/totalWord
            percentage = float("{0:.3f}".format(percentage))

        return (percentage)

   

    def percenageWordsLength(self,input,totalLength):


        #qui calcola la probabilita di pescare una parola con la
        #lunghezza minore di 9
        #es ["a","b","c","AntonioLonga"] ris = 75%
        
        """
        totalWord=0
        wordsMore=0
        for word in input:
            totalWord=totalWord+1
            if (len(word)<9):
                wordsMore=wordsMore+1

        if totalWord==0:
            percentage=0
        else:
            percentage=(100*wordsMore)/totalWord
            percentage=float("{0:2f}".format(percentage))

        return (percentage)
        """

        
        # qui calcolo la lunghezza media delle parole!
       
        #totalLength=0
        #for word in input:
         #   totalLength=totalLength+len(word)

        if totalLength==0:
            print ("c'è qualcosa che non va nel metodo percenageWordsLength")
            average=0
        else:
            average=totalLength/len(input)
        return (average)
        



    def percentageRareBigram(self,input):
        countRareBigrams=0
        totalBigrams=0
        bigramSet=getRareBigramFromFile()

        

        for word in input:
            for i in range(0,len(word)-1):
                totalBigrams=totalBigrams+1
                bigram=(word[i]+word[i+1])
                bigram=bigram.upper()
                
                
                if bigram in bigramSet:
                    countRareBigrams=countRareBigrams+1
    
        if totalBigrams==0:
            percentage=0
        else:
            percentage=(100*countRareBigrams)/totalBigrams
            percentage=float("{0:2f}".format(percentage))
        return (percentage)


def getRareBigramFromFile():
    with open("rareBigram/rareBigram.txt") as f:
        for bigram in f:
            big=re.match("(\w\w)(\w*)",bigram)
            if big:
                rareBigram.add(big.group(1))
            
    f.close()
            
    return (rareBigram)




