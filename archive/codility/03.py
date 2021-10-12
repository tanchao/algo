__author__ = 'tanchao@github'


def solution(A, B, C, D):
    F = [A, B, C, D]
    F.sort()
    # best shuffle once sorted: F(S) = [F[1], F[2], F[0], F[3]]
    return abs(F[1] - F[2]) + abs(F[2] - F[0]) + abs(F[0] - F[3])

if __name__ == '__main__':
    print solution(-1, 3, 5, 5)
