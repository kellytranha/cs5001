import re


def add_word_to_word_list(word_list, word):
    word_list.append("".join(word))
    word.clear()


def sentence_to_word_list(sentence):
    word_list = []
    word = []
    for ch in sentence:
        if ch.isalnum() or ch == "'":
            word.append(ch)
        elif ch == ",":
            if word:
                add_word_to_word_list(word_list, word)
            word_list.append("COMMA")
        elif word:
            add_word_to_word_list(word_list, word)
    if word:
        add_word_to_word_list(word_list, word)
    return word_list


def sentences_to_word_lists(sentences):
    return [sentence_to_word_list(sentence) for sentence in sentences]


class TextCleaner:
    def __init__(self):
        self.replacements = {
            "mr.": "mr"
        }

    def clean(self, text):
        text = re.sub("[^a-z'.\s,]", " ", text.lower())
        for to_be_replaced, replacement in self.replacements.items():
            text = text.replace(to_be_replaced, replacement)
        sentences = []

        for line in filter(None, text.splitlines()):
            for sentence in line.split("."):
                if sentence:
                    sentences.append(sentence.strip())

        return sentences_to_word_lists(sentences)