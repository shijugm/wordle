
green = [' ' , ' ' , ' ' , ' ' , ' ' ]
orange = []
orange_loc  =  [[] , [] , [] , [] , []]
black = []
used = []


def buildalphabetScore(wordslist):

    alphabetsScore = {}
    for word in wordslist:
        # print(f"counting alphabest for {word}")
        alphabetlist = [x for x in word]
        # print(alphabetlist)
        distinctset = set(alphabetlist)
        # print(distinctset)
        distinctlist = list(distinctset)
        # print(distinctlist)
        
        for alphabets in distinctlist:
            # print(f"alphabets = {alphabets}")
            for alphabet in alphabets:
                if alphabet in alphabetsScore:
                    alphabetsScore[alphabet] = alphabetsScore[alphabet] + 1
                else:
                    alphabetsScore[alphabet] = 1 
    return alphabetsScore      
    

def setwordScore(wordslist , alphabetsScore):

    wordsScore = {}
    for word in wordslist:
        wordscore = 0 
        for alphabet in word:
            wordscore = wordscore + alphabetsScore[alphabet]
        wordsScore[word] =  wordscore
    return wordsScore


def getWordWithBestScore(wordsScore  ):
    sorted_x = sorted(wordsScore.items() , key=lambda kv:kv[1] , reverse=True )

    # If the word list is large then avoid picking words with repetitve alphabets
    if  len(wordsScore) <=25:
        bestword = sorted_x[0][0]
    else:
        for word in sorted_x:
            if len(word[0]) == len(list(set(word[0]))):
                bestword = word[0]
                return bestword

    return bestword

def applyresponse(wordslist , responselist):
    # green  = [ 'S' , 'H' ,' ' ,' ', ' ' ]
    # # orange = [['A' , 3]]
    # orange = ['A', 'N']
    # black = [ 'E',   'R' , 'O', 'R' , 'U', 'T', 'I', 'C', 'U', 'O', 'D', 'L', 'G' , 'P']
    # used = ['AEROS' ]
    response = []

    for words in wordslist:
        skip = 'N'
        alphabet =  list(words)

        print(f"TESTING word ------ {words}")
        # remove used words
        if words in used:
            skip = 'Y'
        
        print(f"    After test of USED words skip = {skip}")


        # apply green 
        if skip == 'N':
            
            # print(f"    test green for {alphabet}")
            for i in range(0,5):
                if green[i] != ' ' and  alphabet[i] != green[i]:
                    skip = 'Y'
                    pass
        
        print(f"    After test of GREEN skip = {skip}")

        # apply orange
        if skip == 'N':
            for orange_alphabet in orange:
                if orange_alphabet != ' ' and orange_alphabet not in alphabet:
                    skip = 'Y'    
                    pass                

        print(f"    After test of ORANGE skip = {skip}")

        # apply orange location 
        if skip == 'N':
            
            print(f"    {orange_loc } ")

            for i in range(0,5):
                if  len(orange_loc[i]) > 0 and  alphabet[i]  in  orange_loc[i]:
                    print(f" location {i} has some values to compare")
                    print(f"comparing {alphabet[i]} not in  {orange_loc[i]} returned true")
                    skip = 'Y'
                    pass            

        print(f"    After test of ORANGE location skip = {skip}")

        # apply black
        print(f"    {black } ")
        if skip == 'N':
            for black_alphabet in black:
                if black_alphabet  in alphabet:
                    skip = 'Y'    
                    pass      

                
        print(f"    After test of BLACK skip = {skip}")

        # add to dict 
        if skip == 'N':
            response.append(words)

    return response




def score(wordslist):
    
    

    responselist = [('R' , 'G') , ('E' , 'O') , ('A' , 'B') , ('M' , 'B') , ('S' , 'B') ]

    filteredwords = applyresponse(wordslist, responselist)
    alphabetsScore = buildalphabetScore(filteredwords)
    filteredwordsScore  = setwordScore(filteredwords, alphabetsScore)
    print(f"filtered words count = {len(filteredwords)}")
    print(alphabetsScore)

    word = getWordWithBestScore(filteredwordsScore )

    if len(filteredwords) <= 10:
        print( f"Less than 10 possible words {filteredwords}") 

    print(f"Recommended word  : {word}")
    print(f"orange loc = {orange_loc}")

    return filteredwords


def buildfilter(alphabet, position, response):
    if response == 'G':
        green[position] = alphabet
    if response == 'B':
            black.append(alphabet)  
    if response == 'O':
        orange.append(alphabet)
        orange_loc[position].append( alphabet)



if __name__ == '__main__':
    
    allWords = [] 

    with open('/Users/shijum/git/wordle/resources/all5letter_words') as file:
    # with open('/Users/shijum/git/wordle/resources/all5letter_words_test') as file:
        for line in file:
            for words in line.split():
                allWords.append(words.rstrip())   

    green = [ 'T' , ' ' , ' ' , ' ' , ' ' ]
    orange = ['E' , 'R' , 'T' , 'U' ]
    orange_loc  =  [[] , ['E' , 'R'] , ['R' , 'T' , 'E', 'U']  , ['U', 'R'] , ['T']]
    black = ['A' , 'S' ,  'O' , 'N' , 'I', 'P' , 'I' , 'N' , 'C']
    used = ['AEROS']

    #  allWords = ['LOWLY'] 
    score(allWords)

    