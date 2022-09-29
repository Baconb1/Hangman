"""
Project: Hangman.py
Author: Brock Bacon
Date: 9/29/2022
"""

import random
words = ['chicken', 'dog', 'cat', 'mouse', 'frog']
lives_remaining = 10
guessed_letters = ''
def pick_a_word():
    word_position = random.randint(0, len(words) - 1)
    return words[word_position]
print(pick_a_word())