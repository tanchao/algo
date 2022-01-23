#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

__author__ = 'tanchao'
islands = {}


class city(object):
    def __init__(self, length=0):
        self.length = length

    def build(self, f, t):
        pass

    def road(self, f, t):
        pass

    def find(self, i):
        pass

    def count(self):
        pass


class Island(object):
    def __init__(self, name=''):
        self.name = name
        self.to_island = dict()
        self.from_island = dict()
        self.connect_islands = set()

    def add_to_island(self, island, date):
        self.to_island[island] = date

    def add_from_island(self, island, date):
        self.from_island[island] = date

    def add_connect_island(self, island):
        return self.connect_islands.add(island)


def check(from_, to_, d):
    from_island = islands[from_]
    to_island = islands[to_]


def build(from_, to_, d):
    from_island = islands[from_]
    to_island = islands[to_]
    from_island.add_to_island(to_island)
    to_island.add_from_island(from_island)
    from_island.add_connect_island(to_island)
    to_island.add_connect_island(from_island)
    islands[from_] = from_island

def construct(query, d):
    act, i_from, i_to = query.split()
    if act == 'build':
        build(i_from, i_to, d)
    if act == 'check':
        check(i_from, i_to, d)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        with open(sys.argv[3]) as inputs:
            input_data = inputs.readlines()
        n, q = map(int, input_data[0].split())
        islands = {}
        for i in range(1, n + 1):
            islands[str(i)] = Island(str(i))
        for i in range(q):
            construct(input_data(i + 1), i + 1)