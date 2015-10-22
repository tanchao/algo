#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

import sys


def travel_profile(hotels, reqs):
    hotels.sort(key=lambda hotel: len(hotel['facilities']), reverse=True)
    for req in reqs:
        res = ''
        for hotel in hotels:
            if hotel['price'] <= req['price'] and comp(req['facilities'], hotel['facilities']):
                if res:
                    res += ' ' + hotel['id']
                else:
                    res += hotel['id']
        print res


def comp(l1, l2):
    for i in l1:
        if i not in l2:
            return False
    return True


if __name__ == '__main__':
    arg = sys.argv[-1]  # get input file name
    hotels, reqs = [], []
    with open(arg, 'r') as input_file:
        n = int(input_file.readline())
        for i in xrange(n):
            line = input_file.readline()
            lines = line.split()
            hotel = {'id': lines[0], 'price': int(lines[1]), 'facilities': lines[2:]}
            hotels.append(hotel)
        m = int(input_file.readline())
        for i in xrange(m):
            line = input_file.readline()
            lines = line.split()
            req = {'price': int(lines[0]), 'facilities': lines[1:]}
            reqs.append(req)
    travel_profile(hotels, reqs)