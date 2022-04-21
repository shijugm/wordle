import globals


def update_used_word(word):
    globals.used.append(word)


def update_green(alphabet , position): 
    globals.green[position] = alphabet


def update_orange(alphabet , position):
    globals.orange.append(alphabet)
    globals.orange_loc[position].append( alphabet)


def update_black(alphabet , position):
    globals.black.append(alphabet)  


def curate_response(response):
    curated_response = ""
    if response.upper() == 'G' or response == '0':
        curated_response = 'G'
    elif response.upper() == 'B' or response == '1':
        curated_response = 'B'
    if response.upper() == 'O' or response == '2':
        curated_response = 'O'

    return curated_response 


    
def update_configs(word , alphabet, position, response):

    # curated_value = ""
    curated_value = curate_response(response)

    if curated_value == 'G':
        update_green(alphabet, position)
    if curated_value == 'B':
        update_black(alphabet, position)        
    if curated_value == 'O':
        update_orange(alphabet, position)


def merge_black_list():
    # Remove alphabets in black which are also present in Green or Orange 
    merged_black = []
    for i in globals.black:
        if i not in globals.green and i not in globals.orange:
            merged_black.black.append(i)
    globals.black  = merged_black.black
