

def calculate_word_score(words_list , alphabets_score):

    wordsScore = {}
    for word in words_list:
        wordscore = 0 
        for alphabet in word:
            wordscore = wordscore + alphabets_score[alphabet]
        wordsScore[word] =  wordscore
    return wordsScore