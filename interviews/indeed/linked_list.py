#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

"""
Implement a linked array, where each node of a list contains a fixed size array.
"""


class FixedArray:
    def __init__(self, s=10):
        self.size = s
        self.array = [None] * self.size


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return 'Node [' + str(self.value) + ']'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        current = Node(value=val)
        if self.head is None:
            self.head = current
            self.tail = self.head
        elif self.head == self.tail:
            self.tail = current
            self.head.next = self.tail
        else:
            self.tail.next = current
            self.tail = self.tail.next

    def __str__(self):
        if self.head is not None:
            current = self.head
            out = 'LinkedList [\n' + str(current.value) + '\n'
            while True:
                if current.next is None:
                    break
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'


if __name__ == '__main__':
    pass