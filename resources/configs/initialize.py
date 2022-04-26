import resources.configs.globals as globals
import os
from pathlib import Path

def initialize_globals():     

    globals.green = [' ' , ' ' , ' ' , ' ' , ' ' ]
    globals.orange = []
    globals.black = [] 
    globals.orange_loc  =  [[] , [] , [] , [] , []]
    globals.used = []


def fetch_master_list():

    cwd = Path.cwd()
    filename = os.path.join(cwd, 'resources/data/all5letter_words')
    print(filename)

    allWords = []

    with open(filename) as file:
        for line in file:
            for words in line.split():
                allWords.append(words.rstrip())   
    
    return allWords

