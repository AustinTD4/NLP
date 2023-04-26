
import numpy as np
from sklearn.preprocessing import normalize
from generate import GENERATE
import random
import codecs

vocab = codecs.open("brown_vocab_100.txt")

#load the indices dictionary
word_index_dict = {}
for i, line in enumerate(vocab):
    #TODO: import part 1 code to build dictionary
    word_index_dict[line.rstrip('\n')] = i


f = codecs.open("brown_100.txt")

dim=len(word_index_dict)

#TODO: initialize numpy 0s array

counts = counts = np.zeros((dim,dim))

#TODO: iterate through file and update counts

previous_word = '<s>'
for line in f:
    line=line.lower().split()
    for word in line[1:]:
        previous_word_index=word_index_dict[previous_word]
        current_word_index=word_index_dict[word]
        counts[previous_word_index,current_word_index]+=1
        previous_word=word

#TODO: normalize counts
counts+=0.1
probs = normalize(counts, norm='l1', axis=1)


#TODO: writeout bigram probabilities

with open('smooth_probs.txt', 'w') as f:
    
    pairs = [('all', 'the'), ('the', 'jury'), ('the', 'campaign'), ('anonymous', 'calls')]
    for pair in pairs:
        prev_word, curr_word = pair
        prev_word_index = word_index_dict[prev_word]
        curr_word_index = word_index_dict[curr_word]
        f.write(f"{probs[prev_word_index, curr_word_index]:.8f}\n")

f.close()


#TODO: sentence bigram probabilities


f=open("toy_corpus.txt")


#TODO: iterate through file and update counts
sentprob_list=[]
perplexity=[]
previous_word = '<s>'

for line in f:
    line=line.lower().split()
    sent_len = len(line)
    sentprob = 1

    for word in line[1:]:
        previous_word_index=word_index_dict[previous_word]
        current_word_index=word_index_dict[word]
        wordprob=probs[previous_word_index,current_word_index]
        sentprob*=wordprob
        previous_word=word
    perplexity.append(1.0/(pow(sentprob, 1.0/(sent_len-1))))
    sentprob_list.append(sentprob)


    
f.close()        


generated=[GENERATE(word_index_dict, probs, model_type='bigram', max_words='10', start_word='the')]

