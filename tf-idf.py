#! /usr/bin/env python
#-*- coding: utf-8-*-

import math

from operator import itemgetter



def freq(word, document):
    return document.split(None).count(word)


def word_count(document):
    return len(document.split(None))


def df(word, documentlist):
    """
    document frequence.
    """
    count = 0

    for document in documentlist:
        if freq(word, document) > 0:
            count += 1
    return count


def tf(word, document):
    """tf(i, j) = f(t(i), d(j))
    a word of a document 's frequence.
    """
    return (freq(word, document) / float(word_count(document)))


def idf(word, documentlist):
    """
    inverse document frequence.
    """
    return math.log(len(documentlist) / float(df(word, documentlist) + 1))


def tfidf(word, document, documentlist):
    """tf * idf"""
    return (tf(word, document) * idf(word, documentlist))


if __name__ == "__main__":

    documentlist = []
    words = {}

    f = open("test_sohu_news_data", 'r')

    for line in f:
        document = line.split('\t')[1]

        documentlist.append(document)
    f.close()

    documentNumber = 0

    for word in documentlist[documentNumber].split():
        words[word] = tfidf(word, documentlist[documentNumber], documentlist)


    f1 = open("news_tfidf", 'a')


    for item in sorted(words.items(), key=itemgetter(1), reverse=True):

        f1.write("\n%f <= %s" % (item[1], item[0]))
    f1.close()
