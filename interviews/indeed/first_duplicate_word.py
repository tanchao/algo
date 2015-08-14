#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def first_dup_word(text):
    texts = text.strip().split()
    words = set()
    if len(texts) > 2:
        for word in texts:
            if word in words:
                return word
            words.add(word)
    return ''

if __name__ == '__main__':
    pass