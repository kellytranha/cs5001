from word_ladder import WordLadder, gen_words
from word_ladder_app import load_words


wordlist = load_words()


def test_make_ladder():
    w1 = "angel"
    w2 = "devil"
    assert WordLadder(w1, w2, wordlist[len(w1)]).make_ladder().items == ["angel",
        "anger", "aeger","leger","lever", "level", "devel", "devil"]
    w1 = "cat"
    w2 = "hat"
    assert WordLadder(w1, w2, wordlist[len(w1)]).make_ladder().items == ["cat",
        "hat"]
    w1 = "love"
    w2 = "hate"
    assert WordLadder(w1, w2, wordlist[len(w1)]).make_ladder().items == ["love",
        "hove", "have", "hate"]


