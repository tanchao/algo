#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.caches = dict()
        self.orders = []


    # @return an integer
    def get(self, key):
        if key in self.orders:
            self.orders.remove(key)  # put key to lastest position
            self.orders.append(key)
            return self.caches[key]
        return -1


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.orders:
            self.caches[key] = value
            self.orders.remove(key)  # put key to lastest position
            self.orders.append(key)
        else:
            if len(self.orders) < self.capacity:  # new
                self.orders.append(key)
                self.caches[key] = value
            else:  # move oldest
                self.caches.pop(self.orders[0])
                self.caches[key] = value
                self.orders = self.orders[1:]
                self.orders.append(key)


if __name__ == '__main__':
    pass