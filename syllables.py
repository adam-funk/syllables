#!/usr/bin/env python3
import fileinput

import nltk
import argparse
from nltk.corpus import cmudict

# https://www.nltk.org/_modules/nltk/corpus/reader/cmudict.html

vowels = ['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']

# TODO simplify to first character?


def count_from_pronunciation(pronunciation):
    # vowel can have 1, 2, or 0 appended to indicate stress
    return len([phoneme for phoneme in pronunciation if phoneme[:2] in vowels])


def count_from_word(word):
    try:
        pronunciations = cmudict.dict()[word.lower()]
    except KeyError:
        return []
    return [count_from_pronunciation(pronunciation) for pronunciation in pronunciations]


def count_from_word_to_string(word):
    syllable_counts = count_from_word(word)
    if syllable_counts:
        return ','.join([str(sc) for sc in syllable_counts])
    return '0'


def filter_by_syllable(words, n):
    return [word for word in words if n in count_from_word(word)]


def filter_by_syllables(words, nn):
    return [word for word in words if set(nn).intersection(count_from_word(word))]


if __name__ == '__main__':
    oparser = argparse.ArgumentParser(description="syllable filter",
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    oparser.add_argument("-n", dest="syllable_list",
                         type=str,
                         help="comma-separated list of nbr of syllables")

    oparser.add_argument('-c', dest='count',
                         default=False,
                         action='store_true',
                         help='add syllable count after each word')

    oparser.add_argument('-b', dest='retain_blank',
                         default=False,
                         action='store_true',
                         help='retain blank lines in output')

    oparser.add_argument('files', metavar='FILE', nargs='*',
                         help='input files')

    options = oparser.parse_args()

    if options.syllable_list:
        keep_counts = [int(s) for s in options.syllable_list.split(',')]

        for line in fileinput.input(options.files):
            tokens = line.strip().split()
            result = ' '.join(filter_by_syllables(tokens, keep_counts))
            if result or options.retain_blank:
                print(result)

    elif options.count:
        for line in fileinput.input(options.files):
            tokens = line.strip().split()
            result = ' '.join([' '.join([token, count_from_word_to_string(token)]) for token in tokens])
            if result or options.retain_blank:
                print(result)

