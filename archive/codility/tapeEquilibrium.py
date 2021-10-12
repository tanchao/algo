__author__ = 'tanchao@github'


def tapeEquilibrium(A):
    left, right, total = A[0], 0, sum(A)
    res = abs(total - left * 2)
    for i in range(1, len(A) - 1):  # N > P > 0
        left += A[i]
        right = total - left
        if abs(left - right) < res:
            res = abs(left - right)
        if res == 0:
            break
    return res


if __name__ == '__main__':
    tapeEquilibrium([1000, 1000])
