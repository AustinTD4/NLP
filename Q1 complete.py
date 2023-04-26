import numpy as np
from generate import GENERATE


vocab = open("brown_vocab_100.txt")

#load the indices dictionary
word_index_dict = {}
for i, line in enumerate(vocab):
    #TODO: import part 1 code to build dictionary
    word_index_dict[line.rstrip('\n')] = i


f = open("brown_100.txt")

#TODO: initialize counts to a zero vector

counts = np.zeros(len(word_index_dict))

#TODO: iterate through file and update counts


for line in f:
    line = line.lower().split()  
    for word in line:
        counts[word_index_dict[word]]+=1

f.close()

#TODO: normalize and writeout counts. 

probs = counts / np.sum(counts)

#TODO: write your new probs vector to a file called unigram_probs.txt
with open('unigram_probs.txt', 'w') as f:

    for i in probs:
        f.write(f"{i:.8f}\n")
        
        
#Question 6

#TODO: find sentence probability
f = open("toy_corpus.txt")
sent_len=[]
sentprob_list=[]
for line in f:
    line = line.lower().split()  
    sentprob = 1
    sent_len.append(len(line))
    for word in line:
        wordprob=probs[word_index_dict[word]]
        sentprob *= wordprob
    sentprob_list.append(sentprob)


#TODO: perplexity


perplexity=[1/pow(sentprob_list[i], 1.0/sent_len[i]) for i in range(len(sentprob_list))]

f.close()


#TODO: generate 10 senteces


generated_sent=[GENERATE(word_index_dict, probs, model_type='unigram', max_words=10, start_word='the') for i in range(10)]

