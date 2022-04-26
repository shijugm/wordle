import resources.configs.globals as globals 
from score.rescore import refresh_words_list_and_rescore


def getWordWithBestScore(wordsScore):
    sorted_wordscore = sorted(wordsScore.items() , key=lambda kv:kv[1] , reverse=True )
    print(sorted_wordscore)
    
    # If the word list is large then avoid picking words with repetitve alphabet to get a wider range of alphabets
    if  len(wordsScore) <=25:
        bestword = sorted_wordscore[0][0]
    else:
        for word in sorted_wordscore:
            if len(word[0]) == len(list(set(word[0]))):
                bestword = word[0]
                return bestword

    return bestword



def recommend(words_list):

    filteredwords ,  filteredwordsScore, alphabetsScore = refresh_words_list_and_rescore(words_list)

    print(f"filtered words count = {len(filteredwords)}")
    print(alphabetsScore)

    word = getWordWithBestScore(filteredwordsScore )

    if len(filteredwords) <= 10:
        print( f"Less than 10 possible words {filteredwords}") 

    print(f"Recommended word  : {word}")
    print(f"globalvars.orange loc = {globals.orange_loc}")

    return filteredwords

