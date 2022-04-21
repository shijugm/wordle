
import globals


def rebuild(wordslist ):

    refined_list = []

    for words in wordslist:
        skip = 'N'
        alphabet =  list(words)

        print(f"TESTING word ------ {words}")
        # skip globalvars.used words
        if words in globals.used:
            skip = 'Y'
        
        print(f"    After test of globalvars.used words skip = {skip}")


        # apply green 
        if skip == 'N':
            
            # print(f"    test green for {alphabet}")
            for i in range(0,5):
                if globals.green[i] != ' ' and  alphabet[i] != globals.green[i]:
                    skip = 'Y'
                    pass
        
        print(f"    After test of GREEN skip = {skip}")

        # apply globalvars.orange
        if skip == 'N':
            for globals.orange_alphabet in globals.orange:
                if globals.orange_alphabet != ' ' and globals.orange_alphabet not in alphabet:
                    skip = 'Y'    
                    pass                

        print(f"    After test of globalvars.orange skip = {skip}")

        # apply globalvars.orange location 
        if skip == 'N':
            
            for i in range(0,5):
                if  len(globals.orange_loc[i]) > 0 and  alphabet[i]  in  globals.orange_loc[i]:
                    print(f" location {i} has some values to compare")
                    print(f"comparing {alphabet[i]} not in  {globals.orange_loc[i]} returned true")
                    skip = 'Y'
                    pass            

        print(f"    After test of globalvars.orange location skip = {skip}")

        # apply globalvars.black
        if skip == 'N':
            for globals.black_alphabet in globals.black:
                if globals.black_alphabet  in alphabet:
                    skip = 'Y'    
                    pass      

                
        print(f"    After test of globalvars.black skip = {skip}")

        # add to dict 
        if skip == 'N':
            refined_list.append(words)

    return refined_list

