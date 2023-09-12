#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]

    # Calculate the length of the string
    length = len(sentence)

    # Return a tuple with length and first character
    return (length, first_char)
