"""
Write a function which takes a string and make an acronym of it. Steps to follow:
 - Split string to words by space char.
 - Take every first letter from word in given string
 - Uppercase it
 - Join them together
"""

def make_acronym(sentence):
    list_of_words = sentence.split(" ")
    output = ""
    for word in list_of_words:
        output += word[0].capitalize()
    return output

print(make_acronym("Sample sentence here"))