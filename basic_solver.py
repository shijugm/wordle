import initialize 
import globals
from user_interaction import get_input_word
from user_interaction import get_word_response
from recommender import basic_recommender 



def basic_solver():
    initialize.initialize_globals()
    allWords = initialize.fetch_master_list()
    print(f"used = {globals.used}")
    basic_recommender.recommend(allWords)

    iter1_word = get_input_word(1)
    get_word_response(iter1_word)
    
    basic_recommender.recommend(allWords)

    print(f" green = {globals.green}")
    print(f" orange = {globals.orange}")   
    print(globals.orange_loc)  
    print(f" black = {globals.black}")
    print(globals.used)


    for i in range(0,5):
        iter_n_word =  get_input_word()
        get_word_response(iter_n_word)

        print(globals.green)
        print(globals.orange)   
        print(globals.orange_loc)  
        print(globals.black)
        print(globals.used)

        filteredwords = basic_recommender.recommend(allWords)
        allWords = filteredwords


if __name__ == '__main__':
    basic_solver()
