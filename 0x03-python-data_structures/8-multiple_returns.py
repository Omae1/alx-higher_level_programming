#!/usr/bin/python3
def multiple_returns(sentence):
    len_of_sen = len(sentence)

    if (len_of_sen == 0):
        new_tuple = (len_of_sen, None)
    else:
        new_tuple = (len_of_sen, sentence[0])

    return (new_tuple)
