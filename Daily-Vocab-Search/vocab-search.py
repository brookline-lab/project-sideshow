# This script will perform a number of searches on bing.com using the Edge browser
# It assumes the user is on Windows and is logged into Edge with their Microsoft account

# If the user is logged in, they will accumulate Microsoft Points as an added 
# bonus to learning new words!
import os
import random
import time

word_list = "vocabulary.txt"
number_of_searches = 10
search_url = "https://www.bing.com/search?q=define%3A"
sleep_timer = 3     # Allow plenty of time for each browser instance to finish loading

# Since I'm unaware of how bing provides search results, these searches will be
# preceded by the term "define:" to hopefully avoid poisoning the users future 
# search recommendations
#
# The default word list is a few thousand entries 6 - 8 characters long
def start_search(list_length):
    terms = []
    command = "start msedge "
    dictionary = open(word_list).readlines()

    # Builds a list of random words to match the number of searches to be performed
    for selection in range(0, list_length):
        terms.append(random.choice(dictionary))


    for i in range(0,list_length):
        query = search_url + terms[i]
        os.system(command + query)
        time.sleep(sleep_timer)

if __name__ == '__main__':
    start_search(number_of_searches)