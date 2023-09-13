
# import re ----> THIS LINE IS NECESSARY ONLY AT THE SECOND SOLUTION

import string

def is_pangram(sentence):
    #sentence = re.sub(r'[^\w\s]','',sentence) ----> THIS LINE IS NOT NECESSARY
    sentence = sentence.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in sentence:
            return False
    return True

"""
def is_pangram(sentence):
    # Remove all punctuation
    sentence = re.sub(r'[^\w\s]','',sentence)
    # convert the sentence to lowercase
    sentence = sentence.lower()
    # Create a set of the alphabet
    alphabet = set(string.ascii_lowercase)
    # Iterate over the characters in the sentence
    for char in sentence:
        # If the character is in the alphabet set, remove it
        if char in alphabet:
            alphabet.remove(char)
    # Return whether or not the alphabet set is empty (i.e. all letters were used)
    return len(alphabet) == 0
*/
"""

sentence = input("Enter a sentence to check if it is a pangram: \n")
sentence = str(sentence)
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
    

