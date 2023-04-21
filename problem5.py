# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:40:22 2023

@author: austi
"""
import numpy as np
import codecs

vocab = codecs.open("brown_vocab_100.txt")

word_index_dict = {}
for i, line in enumerate(vocab):
    word_index_dict[line.rstrip('\n')] = i

f = codecs.open("brown_100.txt")

counts = np.zeros((len(word_index_dict),len(word_index_dict),len(word_index_dict)))
for line in f:
    first_word = "<s>"
    line = line.lower().split()
    second_word = line[1]
    for word in line[2:]:
        counts[word_index_dict[first_word]][word_index_dict[second_word]][word_index_dict[word]] += 1
        first_word = second_word
        second_word = word
f.close()

counts_sum = np.sum(counts, axis=2, keepdims=True)
probs = counts / counts_sum
itp = probs[word_index_dict['in']][word_index_dict['the']][word_index_dict['past']]
itt = probs[word_index_dict['in']][word_index_dict['the']][word_index_dict['time']]
tjs = probs[word_index_dict['the']][word_index_dict['jury']][word_index_dict['said']]
tjr = probs[word_index_dict['the']][word_index_dict['jury']][word_index_dict['recommended']]
jst = probs[word_index_dict['jury']][word_index_dict['said']][word_index_dict['that']]
at = probs[word_index_dict['agriculture']][word_index_dict['teacher']][word_index_dict[',']]
group = [itp,itt,tjs,tjr,jst,at]

counts2 = counts+0.1
counts_sum2 = np.sum(counts2, axis=2, keepdims=True)
probs2 = counts2 / counts_sum2
itp2 = probs2[word_index_dict['in']][word_index_dict['the']][word_index_dict['past']]
itt2 = probs2[word_index_dict['in']][word_index_dict['the']][word_index_dict['time']]
tjs2 = probs2[word_index_dict['the']][word_index_dict['jury']][word_index_dict['said']]
tjr2 = probs2[word_index_dict['the']][word_index_dict['jury']][word_index_dict['recommended']]
jst2 = probs2[word_index_dict['jury']][word_index_dict['said']][word_index_dict['that']]
at2 = probs2[word_index_dict['agriculture']][word_index_dict['teacher']][word_index_dict[',']]
group2 = [itp2,itt2,tjs2,tjr2,jst2,at2]

print(group)
print(group2)


