from text_cleaner import sentence_to_word_list


def test_sentence_to_word_list():
    sentence = "it's a dead scene, but that's a good thing"
    word_list = ["it's", "a", "dead", "scene", "COMMA", "but", "that's", "a",
                 "good", "thing"]
    assert sentence_to_word_list(sentence) == word_list
