

from doctest import master


 
def readFile_bigger():
    allLines = []
    with open('/Users/shijum/git/wordle/resources/words_bigger') as file:
        for line in file:
            for words in line.split():
                allLines.append(words.rstrip())   
    return allLines


def writeFile(wordlist):
    with open('/Users/shijum/git/wordle/resources/all5letter_words', 'w') as f:
        for item in wordlist:
            f.write("%s\n" % item)


def all5letterwords(allwords):
    masterlist = [word for word in allwords if len(word) == 5]

    return masterlist

def start():
    pass
    print("starting")
    # all_words = ['create', 'cupid' , 'zenea' , 'abase' , 'tacit', 'where' , 'abhor']
    # allLines = readFile()
    # print(allLines)

    allLines = readFile_bigger()
    print(len(allLines))
    masterlist = all5letterwords(allLines)
    print(len(masterlist))

    writeFile(masterlist)

    
if __name__ == '__main__':
    start()