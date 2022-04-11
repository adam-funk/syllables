#!/usr/bin/env python3
import fileinput

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


def filter_by_syllables(words, nn):
    return [word for word in words if set(nn).intersection(count_from_word(word))]

if __name__ == '__main__':
    oparser = argparse.ArgumentParser(description="syllable filter",
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    oparser.add_argument("-n", dest="syllable_list",
                         required=True,
                         type=str,
                         help="comma-separated list of nbr of syllables")

    oparser.add_argument('files', metavar='FILE', nargs='*',
                         help='input files')

    options = oparser.parse_args()

    keep_counts = [int(s) for s in options.syllable_list.split(',')]

    for line in fileinput.input(options.files):
        tokens = line.strip().split()
        print(' '.join(filter_by_syllables(tokens, keep_counts)))
