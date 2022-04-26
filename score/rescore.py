
from score.alphabet_score  import calculate_alphabet_score
from score.word_score import calculate_word_score
from score.rebuild_words_list import rebuild
from filterconfigs import merge_black_list

def refresh_words_list_and_rescore(words_list):
    print(words_list)

    
    merge_black_list()

    filteredwords = rebuild(words_list)

    alphabetsScore = calculate_alphabet_score(filteredwords)
    filteredwordsScore  = calculate_word_score(filteredwords, alphabetsScore)

    return filteredwords ,  filteredwordsScore, alphabetsScore