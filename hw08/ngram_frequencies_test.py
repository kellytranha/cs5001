from pytest import approx
from ngram_frequencies import generate_ngrams, NgramFrequenies


def test_generate_ngrams():
    word_list = ['together', 'COMMA', 'the', 'eerie', 'couple']
    unigrams = generate_ngrams(1, word_list)
    trigrams = generate_ngrams(3, word_list)
    verify = ["together_COMMA_the", "COMMA_the_eerie", "the_eerie_couple"]
    assert unigrams == word_list
    assert trigrams == verify


def test_ngram_freqs_add_item():
    freqs = NgramFrequenies()
    freqs.add_item("COMMA")
    assert len(freqs.freqs) == 1
    assert freqs.freqs["COMMA"] == 1
    freqs.add_item("COMMA")
    assert len(freqs.freqs) == 1
    assert freqs.freqs["COMMA"] == 2
    freqs.add_item("a")
    assert len(freqs.freqs) == 2


def test_ngram_freqs_top_n_counts():
    freqs = NgramFrequenies()
    word_list = ["a", "a", "a", "b", "b", "c", "c", "e", "e", "f"]
    for word in word_list:
        freqs.add_item(word)
    top_4 = freqs.top_n_counts(4)
    top_10 = freqs.top_n_counts(10)
    assert len(freqs.freqs) == 5
    assert len(top_10) == 5
    assert len(top_4) == 4
    assert top_4[0] == ("a", 3)
    assert top_4[-1] == ("e", 2)
    assert top_10[0] == ("a", 3)
    assert top_10[-1] == ("f", 1)


def test_ngram_freqs_top_n_freqs():
    freqs = NgramFrequenies()
    word_list = ["a", "a", "a", "b", "b", "c", "c", "e", "e", "f"]
    for word in word_list:
        freqs.add_item(word)
    top_4 = freqs.top_n_freqs(4)
    top_10 = freqs.top_n_freqs(10)
    assert len(freqs.freqs) == 5
    assert len(top_10) == 5
    assert len(top_4) == 4
    assert top_4[0] == ("a", approx(3/10))
    assert top_4[-1] == ("e", approx(2/10))
    assert top_10[0] == ("a", approx(3/10))
    assert top_10[-1] == ("f", approx(1/10))


def test_ngram_freqs_frequency():
    freqs = NgramFrequenies()
    word_list = ["a", "a", "a", "b", "b", "c", "c", "e", "e", "f"]
    for word in word_list:
        freqs.add_item(word)
    assert freqs.frequency("b") == approx(2/10)
    assert freqs.frequency("c") == approx(2/10)
    assert freqs.frequency("e") == approx(2/10)
    assert freqs.frequency("a") == approx(3/10)
    assert freqs.frequency("f") == approx(1/10)
