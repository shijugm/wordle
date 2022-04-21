

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


def getWordWithBestScore(wordsScore):
    sorted_x = sorted(wordsScore.items() , key=lambda kv:kv[1] , reverse=True )
    # print(f"sorted_x = {sorted_x}")    
    # bestword = max(wordsScore, key=wordsScore.get)
    bestword = sorted_x[0][0]
    for word in sorted_x:
        if len(word[0]) == len(list(set(word[0]))):
            bestword = word[0]
            return bestword
    return bestword

def score(wordslist):
    alphabetsScore = buildalphabetScore(wordslist)
    # print(alphabetsScore)
    wordsScore  = setwordScore(wordslist, alphabetsScore)
    # print(wordsScore)

    word = getWordWithBestScore(wordsScore)
    print(f"Recommended word  : {word}")


if __name__ == '__main__':
    
    allWords = []
    with open('/Users/shijum/git/wordle/resources/all5letter_words') as file:
    # with open('/Users/shijum/git/wordle/resources/all5letter_words_test') as file:
        for line in file:
            for words in line.split():
                allWords.append(words.rstrip())   

    # print(allWords) 
    # wordslist = ['ABCDE', 'ABCDF' , 'ZREAD']
    score(allWords)