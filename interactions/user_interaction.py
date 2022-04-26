
from resources.configs.filterconfigs import update_configs , update_used_word


def get_input_word(iteration = 0 ):
    if iteration == 1:
        input_word = input("Enter word , recommended first word is AEROS : " )
    else:
        input_word = input("Enter word  : " )

    update_used_word(input_word)
    
    return input_word
    

def get_word_response(input_word):
    print("Enter characters  G or 0 for GREEN, 1 or B for BLACK & 2 or O for ORANGE")
    
    input_word_list = list(input_word)
    for i in range(0,len(input_word_list) ):
        response = input(f"enter response for {input_word_list[i]} :  ")
        update_configs(input_word, input_word_list[i], i, response)
    
    
    