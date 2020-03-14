from ngram_frequencies import generate_ngram_freqs
from text_cleaner import TextCleaner


def print_ngram(ngram_type, name, word_lists):
    ngram_freqs = generate_ngram_freqs(ngram_type, word_lists)
    print(f"Top 10 {name}:")
    for ngram in ngram_freqs.top_n_freqs(10):
        print(f"\t{ngram}")


def main():
    with open("corpse_bride.txt", "r") as f:
        content = f.read()

    word_lists = TextCleaner().clean(content)
    print_ngram(1, "unigrams", word_lists)
    print_ngram(2, "bigrams", word_lists)
    print_ngram(3, "trigrams", word_lists)


main()
