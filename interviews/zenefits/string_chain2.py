#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def word_ladder(start, end_len, dic):
    word_queue, cur_word = [], start
    word_queue.append(start)
    while word_queue:
        cur_word = word_queue.pop(0)  # FIFO check words
        if len(cur_word) == end_len:
            if cur_word in dic:
                return True
            else:
                break
        for j in range(len(cur_word)):
            new_word = cur_word[:j] + cur_word[j + 1:]
            if new_word in dic:
                word_queue.append(new_word)
                dic.remove(new_word)
    return False


def longest_chain(w):
    if len(w) < 2:
        return len(w)
    result = 1  # suppose {'a'} returns 1
    wd = dict()
    for word in w:  # group words by length
        word_len = len(word)
        if word_len in wd:
            wd[word_len].add(word)
        else:
            word_set = set()
            word_set.add(word)
            wd[word_len] = word_set
    min_len, max_len = min(wd), max(wd)
    if max_len > min_len:
        for start_length in range(max_len, min_len, -1):
            if start_length in wd:
                for end_length in range(min_len, start_length):
                    if end_length in wd:
                        for begin_word in wd[start_length]:
                            words = w
                            if word_ladder(begin_word, end_length, words):
                                result = max(start_length - end_length + 1, result)
    return result


n = int(raw_input())
_w = []
for i in range(0, n):
    s = raw_input()
    _w.append(s)
res = longest_chain(_w)
print res