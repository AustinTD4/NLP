counts = np.zeros(len(word_index_dict))

with open("brown_100.txt") as f:
    for line in f:
        line = line.lower().replace('<s>', '').replace('</s>', '')

        words = line.split()

        for word in words:
            counts[word_index_dict[word]] += 1

probs = counts / np.sum(counts)

with open('unigram_probs.txt', 'w') as output_file:
    output_file.write(str(probs))
