# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def calc_area(K, L, M, N, P, Q, R, S):
    first_area = (M - K) * (N - L)
    second_area = (R - P) * (S - Q)

    if first_area > 2147483647 or second_area > 214783647:
        return -1

    left = max(L, Q)
    right = min(N, S)
    bottom = max(K, P)
    top = min(M, R)
    intersection_area = 0
    if left < right and bottom < top:
        intersection_area = (right - left) * (top - bottom)

    return first_area + second_area - intersection_area


def recalc_area(K, L, M, N, P, Q, R, S):
    first_area = (M - K) * (N - L)
    second_area = (R - P) * (S - Q)
    left = max(L, Q)
    right = min(N, S)
    bottom = max(K, P)
    top = min(M, R)
    intersection_area = 0
    if left < right and bottom < top:
        intersection_area = (right - left) * (top - bottom)
    total_area = first_area + second_area - intersection_area
    if total_area > 2147483647:
        return -1
    return total_area


if __name__ == '__main__':
    print calc_area(-4, 1, 2, 6, 0, -1, 4, 3)
    print recalc_area(-4, 1, 2, 6, 0, -1, 4, 3)