from queue import Queue
from stack import Stack


def gen_words(word):
    words = []
    for i in range(len(word)):
        for letter in "abcdefghijklmnopqrstuvwxyz":
            words.append(word[:i] + letter + word[i+1:])
    return words


class WordLadder:
    """A class providing functionality to create word ladders"""
    # TODO:
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.
    def __init__(self, w1, w2, wordlist):
        self.w1 = w1
        self.w2 = w2
        self.wordlist = wordlist

    def make_ladder(self):
        queue = Queue()
        stack = Stack()
        stack.push(self.w1)
        queue.enqueue(stack)
        seen = set()
        seen.add(self.w1)
        while not queue.isEmpty():
            stack = queue.dequeue()
            top = stack.peek()
            for word in gen_words(top):
                if word in self.wordlist and word not in seen:
                    duplicate = stack.copy()
                    duplicate.push(word)
                    if word == self.w2:
                        return duplicate
                    queue.enqueue(duplicate)
                seen.add(word)

                        

                    

