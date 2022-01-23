#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def word_ladder(start, end, dic):
    word_queue, word_len = [], len(start)
    word_queue.append((start, 1))
    while word_queue:
        cur_word, cur_len = word_queue.pop(0)  # FIFO check words
        if cur_word == end:
            return cur_len
        for j in range(word_len):
            left, right = cur_word[:j], cur_word[j + 1:]
            new_word = left + right
            if new_word in dic:
                word_queue.append((new_word, cur_len + 1))
                dic.remove(new_word)
    return 0


def longest_chain(w):
    result = 0  # suppose {'a'} returns 0
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
        if not max_len - min_len + 1 == len(wd):  # has break
            sort_len = sorted(wd)
            for j1 in range(1, len(sort_len)):
                j0 = j1 - 1
                if sort_len[j1] - sort_len[j0] != 1:  # break out
                    max_len = j0
        if max_len > min_len:
            for start_length in range(max_len, min_len, -1):
                if start_length in wd:
                    for end_length in range(min_len, start_length):
                        if end_length in wd:
                            for begin_word in wd[start_length]:
                                for end_word in wd[end_length]:
                                    words = w
                                    cur_chain = word_ladder(begin_word, end_word, words)
                                    if cur_chain == start_length - end_length + 1:  # max
                                        return cur_chain
                                    else:
                                        result = max(cur_chain, result)
    return result


n = int(raw_input())
_w = []
for i in range(0, n):
    s = raw_input()
    _w.append(s)
res = longest_chain(_w)
print res