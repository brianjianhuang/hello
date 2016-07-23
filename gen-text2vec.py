#!/usr/bin/python

import os
import sys
import random
import re
import pickle
import json
import numbers

"""
Generate line to tensor and dump to pickle file
"""
def gen_text_tensor(files, word2vec, max_words):
    word_vec_size = len( word2vec.values()[0])
    for file in files:
        out_file = open(file + ".tensor.p", "wb")
        for line in open(file, 'r'):
            print ("line:" , line)
            words = line.lower().split()
            #print ("len word" , len(words))
            if (len(words) ==0):
                continue
            if (len(words) < max_words):
                words = pad_words(words, max_words)
            line_tensor = []
            for word in words:
                line_tensor.append(find_word_vec(word, word2vec, word_vec_size))
            print("line tensor :" , line_tensor)
            pickle.dump(line_tensor, out_file)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def find_word_vec(word, word2vec, word_vec_size):
    if (is_number(word)):
        number_tensor = [0] * word_vec_size
        #just ot normlize the number a bit
        norm_number = 1 -  1 / (float(word) + 1)
        number_tensor[0] = norm_number
        return number_tensor
    else:
        return word2vec.get(word, "empty")

def pad_words(words, length):
    """
    Appends "a" to list to get length of list equal to `length`.
    """
    diff_len = length - len(words)
    if diff_len <= 0:
        return words
    return words  + ["PADDING"] * diff_len

def find_max_words(files):
    """
    Find the longest line, need to pad the shorter ones
    """
    all_num_words = list()
    for file in files:
        num_words =[len(line.split()) for line in open(file, 'r')]
        all_num_words = all_num_words + num_words
    #print (all_num_words)
    return max(all_num_words)

def load_word2vec(word2vec_json_file):
    """ generate the vocabulary lookup """
    word2vec = json.load(open(word2vec_json_file, "r"))
    #print (word2vec["refused"])
    return word2vec

def main():
    files = ['positive.txt', 'negative.txt']
    #files = ['a.txt', 'b.txt']
    word2vec_file = "word2vec_dict.json"

    word2vec = load_word2vec(word2vec_file)
    max_words = find_max_words(files)
    gen_text_tensor(files, word2vec, max_words)
    #print ("generate output file " + output_file)

if __name__ == "__main__":
    main()

