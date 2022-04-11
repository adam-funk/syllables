#!/usr/bin/env python3

import nltk
import argparse
from nltk.corpus import cmudict

# https://www.nltk.org/_modules/nltk/corpus/reader/cmudict.html

vowels = ['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']


def count_from_pronunciation(pronunciation):
    return len([phoneme for phoneme in pronunciation if phoneme in vowels])


def count_from_word(word):
    try:
        pronunciations = cmudict.dict()[word]
    except KeyError:
        return []
    return [count_from_pronunciation(pronunciation) for pronunciation in pronunciations]


def filter_by_syllable(words, n):
    return [word for word in words if n in count_from_word(word)]


# command line options for filtering
# for ignoring unknown words

if __name__ == '__main__':
    pass
