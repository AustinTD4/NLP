import numpy as np
from generate import GENERATE


vocab = open("brown_vocab_100.txt")

#load the indices dictionary
word_index_dict = {}
for i, line in enumerate(vocab):
    #TODO: import part 1 code to build dictionary
    word_index_dict[line.rstrip('\n')] = i


counts = np.zeros(len(word_index_dict))


f = open("brown_100.txt")

#TODO: initialize counts to a zero vector

counts = np.zeros(len(word_index_dict))




for line in f:
        line = line.lower().replace('<s>', '').replace('</s>', '')

        words = line.split()

        for word in words:
            counts[word_index_dict[word]] += 1

f.close()

probs = counts / np.sum(counts)



with open('unigram_probs.txt', 'w') as output_file:
    output_file.write(str(probs))
