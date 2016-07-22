#!/usr/bin/python

import os
import sys
import random
import re
import pickle
import json
"""
Generate a word to vec dictory and dump to a json file

"""
def gen_word_list(files):
        all_words = list()
        for file in files:
                words =[word.lower() for line in open(file, 'r') for word in line.split()]
                all_words = all_words + words
        all_words = all_words + ["PADDING"]
        return list(set(all_words))

def gen_vocabulary(all_words, output_file):
        """ generate the vocabulary lookup """
        word2vec = dict()
        for word in all_words:
                word2vec[word] = [random.random() for r in xrange(2)]
        #print (word2vec)
        json.dump(word2vec, open(output_file, "w"))

def main():
        #files = ['positive.txt', 'negative.txt']
        files = ['a.txt', 'b.txt']
        output_file = "word2vec_dict.json"
        all_words = gen_word_list(files)
        #print ("all_words", all_words)
        gen_vocabulary(all_words, output_file)
        print ("generate output file " + output_file)

if __name__ == "__main__":
        main()

