#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def rotate(L):
    slow, fast, length = L, L, 0
    while fast:
        slow = slow.next
        step = 2
        while fast != None and step > 0:  # fast moves 2 nodes
            fast = fast.next
            length += 1
            step -= 1
    if length < 3: return L
    tail = Node(slow.val)  # copy new tail part
    cur = tail
    while slow.next:
        slow = slow.next
        cur.next = Node(slow.val)
    tail = reverse(tail)
    cur = tail
    while cur:
        print cur.val
        cur = cur.next
    cur = tail
    res, tr = None, None
    flag = length % 2
    length = length / 2
    while length > 0:
        print length, L.val, tail.val
        if tr:
            tr.next = Node(L.val)
            tr = tr.next
        else:  # only at init
            res = Node(L.val)
            tr = res
        tr.next = Node(tail.val)
        tr = tr.next
        L, tail = L.next, tail.next
        length -= 1
    if flag:
        tr.next = Node(L.val)
    return res


def reverse(L):
    cur = L
    pri, tmp = None, None
    while cur:
        tmp = cur.next
        cur.next = pri
        pri = cur
        cur = tmp
    # cur = pri
    # while cur:
    #     print cur.val
    #     cur = cur.next
    return pri


if __name__ == '__main__':
    T1 = Node(1)
    T1.next = Node(2)
    T1.next.next = Node(3)
    T1.next.next.next = Node(4)
    T1.next.next.next.next = Node(5)
    T1.next.next.next.next.next = Node(6)
    T1.next.next.next.next.next.next = Node(7)
    T1.next.next.next.next.next.next.next = Node(8)
    # cur = T1
    # while cur:
    #     print cur.val
    #     cur = cur.next
    R = rotate(T1)
    cur = R
    while cur:
        print cur.val
        cur = cur.next