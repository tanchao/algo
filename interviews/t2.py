#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string, find the longest substring that contains
at most 2 distinct characters.

Example: "ababcbcbaaabbdef"
has a 2-character substring "baaabb" of length 6 (longest)
and a 2-character substring "bcbcb" of lenght 5 (second longest).
"""

__author__ = 'tanchao'


def longest_substr_beta(S):
    res, tmp = '', ''
    slen = len(S)
    if slen <= 2:
        return S
    start, second, mlen = 0, 0, 0
    cache = []
    while mlen < slen - start:
        # print mlen, slen, start, S[start:]
        for i in xrange(start, slen):
            if S[i] in cache:
                tmp += S[i]
            else:
                if len(cache) == 0:  # empty
                    cache.append(S[i])
                    tmp += S[i]
                elif len(cache) == 1:
                    second = i
                    cache.append(S[i])
                    tmp += S[i]
                else:
                    tmp = ''
                    cache = []
                    start = second
                    break
            if len(tmp) > mlen:
                mlen = len(tmp)
                res = tmp
    return res


def longest_substr(S):
    """
    substr shld contain only 2 distinct chars
    :param S:
    :return:
    """
    res, tmp = '', ''
    slen = len(S)
    if slen <= 2:
        return S
    start, second, mlen = 0, 0, 0
    second_flag, second_tmp = True, 0
    cache = []
    while mlen < slen - start:
        for i in xrange(start, slen):
            if S[i] in cache:
                tmp += S[i]
                if len(cache) == 2:
                    if S[i] == cache[1]:  # second char
                        if second_flag and i > second_tmp:
                            second = i
                            second_tmp = i
                            second_flag = False
                    else:  # first char
                        second_flag = True
            else:
                if len(cache) == 0:  # empty
                    cache.append(S[i])
                    tmp += S[i]
                elif len(cache) == 1:
                    second = i
                    cache.append(S[i])
                    tmp += S[i]
                    second_flag = False
                    second_tmp = i
                else:
                    tmp = ''
                    cache = []
                    start = second
                    break
            if len(tmp) > mlen:
                mlen = len(tmp)
                res = tmp
    return res


if __name__ == '__main__':
    print longest_substr('ababcbcbaaabbdef')
    print longest_substr('')
    print longest_substr('aaaaaaaa')
    print longest_substr('aaaaaabbccccccccc')
    print longest_substr('abcabcabcabc')
    print longest_substr('abababbbccabccccaaaaaaadef')
    print longest_substr('ab%%^')
    print longest_substr('ababcbcbaaabbdef')

    print longest_substr_beta('')
    print longest_substr_beta('aaaaaaaa')
    print longest_substr_beta('aaaaaabbccccccccc')
    print longest_substr_beta('abcabcabcabc')
    print longest_substr_beta('abababbbccabccccaaaaaaadef')
    print longest_substr_beta('ab%%^')
    print longest_substr_beta('ababcbcbaaabbdef')