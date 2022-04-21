


def calculate_alphabet_score(wordslist):

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
    