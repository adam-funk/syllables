#!/usr/bin/env python3

import nltk
from nltk.corpus import cmudict

# https://www.nltk.org/_modules/nltk/corpus/reader/cmudict.html

vowels = ['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']


def count_from_pronunciation(pronunciation):
    return len([phoneme for phoneme in pronunciation if phoneme in vowels])


def count_from_word(word):
    # TODO handle KeyError
    # TODO options for single result
    pronunciations = cmudict.dict()['word']
    return [count_from_pronunciation(pronunciation) for pronunciation in pronunciations]

# command line options for filtering
# for ignoring unknown words
