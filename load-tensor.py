#!/usr/bin/python

import os
import sys
import random
import re
import pickle
import json
import numbers

"""
Load the geneated tensor data from the pickle file
"""
def load_tensor(files):
        for file in files:
                tensor_file = open(file, "rb")
                tensors = pickle.load( tensor_file)
                print (file, tensors)


def main():
        files = ['positive.txt.tensor.p', 'negative.txt.tensor.p']
        load_tensor(files)

if __name__ == "__main__":
        main()
