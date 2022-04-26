import resources.configs.initialize as initialize
import resources.configs.globals as globals
from recommender import basic_recommender 


from resources.configs.filterconfigs import update_configs , update_used_word
 



def basic_solver():
    print(f"start initialize")
    initialize.initialize_globals()
    print(f"end initialize")
    allWords = initialize.fetch_master_list()

    print(f"used = {globals.used}")

    print(f" green = {globals.green}")
    print(f" orange = {globals.orange}")   
    print(globals.orange_loc)  
    print(f" black = {globals.black}")
    print(globals.used)


    input_list_of_list = []
    input_list = []


    while True:
        input_string = input('enter iteration and response example AEROS,BGGOG ::: ')
        if input_string == "":
            break
        else:
            input_list = input_string.split(",")
            input_list_of_list.append(input_string.split(","))
            update_used_word(input_list[0])

            input_word_list = list(input_list[0])
            input_response_list = list(input_list[1])

            for i in range(0,len(input_word_list) ):
                update_configs(input_list[0], input_word_list[i], i, input_response_list[i])
    
    print(input_list_of_list)

    print(f"used = {globals.used}")

    print(f" green = {globals.green}")
    print(f" orange = {globals.orange}")   
    print(globals.orange_loc)  
    print(f" black = {globals.black}")

    basic_recommender.recommend(allWords)



if __name__ == '__main__':
    basic_solver()

    