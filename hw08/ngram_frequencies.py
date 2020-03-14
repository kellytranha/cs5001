def generate_ngrams(ngram_type, word_list):
    ngrams = []

    for i in range(0, len(word_list)):
        ngram_list = word_list[i:i+ngram_type] 
        if len(ngram_list) == ngram_type:
            ngram = "_".join(ngram_list)
            ngrams.append(ngram)

    return ngrams


def generate_ngram_freqs(ngram_type, word_lists):
    ngram_freqs = NgramFrequenies()

    for word_list in word_lists:
        for ngram in generate_ngrams(ngram_type, word_list):
            ngram_freqs.add_item(ngram)

    return ngram_freqs


class NgramFrequenies:
    def __init__(self):
        self.freqs = {}
        self.total_count = 0
    
    def add_item(self, item):
        if item not in self.freqs:
            self.freqs[item] = 1
        else:
            self.freqs[item] += 1
        self.total_count += 1
    
    def all_counts(self):
        return sorted(self.freqs.items(), key=lambda x: x[1], reverse=True)
    
    def top_n_counts(self, n):
        return self.all_counts()[:n]

    def top_n_freqs(self, n):
        all_counts = self.all_counts()
        return [(ngram, round(count/self.total_count, 3)) for ngram, count in all_counts][:n]

    def frequency(self, item):
        return self.freqs[item] / self.total_count
    