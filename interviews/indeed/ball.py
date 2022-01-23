#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def ball(balls_, data_):
    for a, b in data_:
        balls_[a - 1], balls_[b - 1] = balls_[b - 1], balls_[a - 1]
    return balls_


def k_ball(balls_, k_):
    origin_balls = balls_
    kb, loop, flag = set(), 0, False
    kb.add(''.join(balls_))
    for j in range(k_):
        balls_ = ball(balls_, data)
        if ''.join(balls_) in kb:  # loop value found
            loop = j
            flag = True
            break
        else:
            kb.add(''.join(balls_))
    if flag:  # init again
        balls_ = origin_balls
        k_ %= loop
        for j in range(k_):
            balls_ = ball(balls_, data)
    return balls_


n, k = map(int, raw_input().split())
balls = ['1', '2', '3', '4', '5', '6', '7', '8']
data = []
for i in range(n):
    x, y = map(int, raw_input().split())
    data.append((x, y))
k_ball(balls, k)
print ' '.join(balls)
