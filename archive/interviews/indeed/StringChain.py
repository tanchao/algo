#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def word_ladder(start, end, dic):
    word_queue, word_len = [], len(end)
    word_queue.append((start, 1))
    while word_queue:
        cur_word, cur_len = word_queue.pop(0)  # FIFO check words
        if cur_word == end:
            return cur_len
        for j in range(word_len):
            left, right = cur_word[:j], cur_word[j + 1:]
            for s in 'abcdefghijklmnopqrstuvwxyz':
                if s != cur_word[j]:
                    new_word = left + s + right
                    if new_word in dic:
                        word_queue.append((new_word, cur_len + 1))
                        dic.remove(new_word)
    return 0


def longest_chain(w):
    result = 0
    if len(w) < 2:
        result = len(w)
    else:
        wd = dict()
        for word in w:
            word_len = len(word)
            if word_len in wd:
                wd[word_len].add(word)
            else:
                word_set = set()
                word_set.add(word)
                wd[word_len] = word_set
        w_len = sorted(wd)
        min_len, max_len = w_len[0], w_len[-1]
        max_chain = max_len - min_len + 1  # max
        for max_word in wd[max_len]:
            for min_word in wd[min_len]:
                words = w
                cur_chain = word_ladder(max_word, min_word, words)
                if cur_chain == max_chain:
                    return cur_chain
    return result


n = int(raw_input())
_w = []
for i in range(0, n):
    s = raw_input()
    _w.append(s)
res = longest_chain(_w)
print res