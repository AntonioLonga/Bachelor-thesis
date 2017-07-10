import os
import re

rareBigram=set()

class AnalysisIdentifier:


    
    def checkObfuscate(self,input):
        #contiene la % di parole con lung minore uguale a 3
        lengthWord=self.lengthWord(input)
        #contiene la % di parole ripetute
        repetuteWord=self.percentageRepetuteWord(input)
        #contiene la % di parole che hanno meno del 25% di vocali
        countVowel=self.percentageCountVowel(input)
        #contiene la % di parole meno lunghe di 9 char
        percenageLength=self.percenageWordsLength(input)
        #contiene la % di bigrammi rari
        rareBigram=self.percentageRareBigram(input)
        print ("% di parole con lung. <= a 3: "+str(lengthWord))
        print ("% di identificatori ripetuti: "+str(repetuteWord))
        print ("% parole con meno del 25% di vocali: "+str(countVowel))
        print ("% di parole con lung. <= a 9: "+str(percenageLength))
        print ("% di bigrammi rari: "+str(rareBigram))


        #range identificatori piu corti di 3 caratteri
        
        #print (self.average(0.93,25.72,lengthWord))
        #print (self.average(15.45,50.35,repetuteWord))
        #print (self.average(20.8,33.75,countVowel))
        #print (self.average(15.43,50.35,percenageLength))
        #print (self.average(0.28,5.65,rareBigram))
        
        length=(self.average(0.93,25.72,lengthWord))
        repetute= (self.average(15.45,50.35,repetuteWord))
        vocali= (self.average(20.8,33.75,countVowel))
        percLength= (self.average(15.43,50.35,percenageLength))
        bigram=(self.average(0.28,5.65,rareBigram))

        totalProbability=(length+repetute+vocali+percLength+bigram)/5
        print ("probabilità che sia offuscato: "+str(totalProbability))

   
    """Return percentage of words that have length less or equals than 3 characters
    This method take an array of words as input, and return percenage of word that
    have length less or equals than tresholder, the tresholder is set on 3"""     
    def lengthWord(self,input):
               
        
        inputLength=len(input)
        lessTresholder=0
        for element in input:
            if len(element) <= 3 :
                lessTresholder=lessTresholder+1

        percentage= (100*lessTresholder)/inputLength
        percentage = float("{0:.2f}".format(percentage))
        return (percentage)

    def average(self,lower,upper, value):

        result= (value-lower)/(upper-lower)

        return result;
        
    
    """Return percentage of repetute words 
    This method take an array of words as input, and return percenage of repetute word  
    """   
    def percentageRepetuteWord(self,input):
    
        wordSet=set()

        for element in input:
            if not(element in wordSet):
                wordSet.add(element)

        inputLength=len(input)
        nonRepetute=len(wordSet)
        repetuteWord=inputLength-nonRepetute        
        percentage=(100*repetuteWord)/inputLength
        percentage = float("{0:.2f}".format(percentage))


        return percentage

    

    """Return precentage of words that has vowel less than 25% 
    """
    def percentageCountVowel(self,input):
        vowels= {"a","e","i","o","u"}
        vowelsCount=0
        totalCharacter=0
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

        percentage=(100*vowelsCount)/totalWord
        percentage = float("{0:.3f}".format(percentage))

        return (percentage)


    def percenageWordsLength(self,input):
        totalWord=0
        wordsMore=0
        for word in input:
            totalWord=totalWord+1
            if (len(word)<9):
                wordsMore=wordsMore+1


        percentage=(100*wordsMore)/totalWord
        percentage=float("{0:2f}".format(percentage))

        return (percentage)
        
        """   
        for word in input:
            totalLength=totalLength+len(word)

        average=totalLength/len(input)
       
        return (percentage)
        """



    def percentageRareBigram(self,input):
        countRareBigrams=0
        totalBigrams=0
        bigramSet=getRareBigramFromFile()

        for word in input:
            for i in range(0,len(word)-1):
                totalBigrams=totalBigrams+1
                bigram=(word[i]+word[i+1])
                if bigram in bigramSet:
                    countRareBigrams=countRareBigrams+1
    
        
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




