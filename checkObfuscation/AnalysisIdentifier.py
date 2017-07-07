import os
import re

rareBigram=set()

class AnalysisIdentifier:

   

    """Return percentage of words that have length less or equals than 3 characters
    This method take an array of words as input, and return percenage of word that
    have length less or equals than tresholder, the tresholder is set on 3 
    """
    def lengthWord(input):
        
        inputLength=len(input)
        lessTresholder=0
        for element in input:
            if len(element) <= 3 :
                lessTresholder=lessTresholder+1

        percentage= (100*lessTresholder)/inputLength
        percentage = float("{0:.2f}".format(percentage))
        return (percentage)

    
    """Return percentage of repetute words 
    This method take an array of words as input, and return percenage of repetute word  
    """   
    def percentageRepertuteWord(input):
    
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

    

    """Return number of vowel in a list of word 
    """
    def percentageCountVowel(input):
        vowels= {"a","e","i","o","u"}
        vowelsCount=0
        totalCharacter=0
        
        for word in input:
            for char in word:
                totalCharacter=totalCharacter+1
                if char in vowels:
                    vowelsCount=vowelsCount+1
        

        percentage=(100*vowelsCount)/totalCharacter
        percentage = float("{0:.3f}".format(percentage))

                
        return (percentage)


    def averageWordsLength(input):
        totalLength=0
        for word in input:
            totalLength=totalLength+len(word)

        average=totalLength/len(input)
        return (average)




    def countRareBigram(input):
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
         
    
