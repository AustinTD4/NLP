# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 08:55:37 2023

@author: austi
"""
word_index_dict = {}

# TODO: read brown_vocab_100.txt into word_index_dict

# TODO: write word_index_dict to word_to_index_100.txt
with open(r'C:\Users\austi\.spyder-py3\brown_vocab_100.txt') as file:
    for count, item in enumerate(file):
        word_index_dict[item.rstrip('\n')] = count
        
print(word_index_dict['all'])
print(word_index_dict['resolution'])
print(len(word_index_dict))
word_index_string = str(word_index_dict)

text = open(r'C:\Users\austi\.spyder-py3\word_to_index_100.txt', 'w')
text.write(word_index_string)
text.close()
