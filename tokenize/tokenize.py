#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 21:06:02 2018

@author: ethanlam
"""


file1 = open("thecandidate.txt", "r")
print(file1.read())
#%%
import nltk

tokenizer = nltk.tokenize.WhitespaceTokenizer()
tokenizer.tokenize(file1.read())

