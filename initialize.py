import globals


def initialize_globals():     

    globals.green = [' ' , ' ' , ' ' , ' ' , ' ' ]
    globals.orange = []
    globals.black = [] 
    globals.orange_loc  =  [[] , [] , [] , [] , []]
    globals.used = []


def fetch_master_list():

    allWords = []
    with open('/Users/shijum/git/wordle/resources/all5letter_words') as file:
    # with open('/Users/shijum/git/wordle/resources/all5letter_words_test') as file:
        for line in file:
            for words in line.split():
                allWords.append(words.rstrip())   
    
    return allWords