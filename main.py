# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:27:06 2020

@author: Sofi Ullah
"""
import nltk
from nltk import tokenize


filein = open("input.txt",'rt')
text = filein.read()
filein.close()
print(text)
sents = (tokenize.sent_tokenize(text))

words = tokenize.word_tokenize(sents[1])
print(words)
