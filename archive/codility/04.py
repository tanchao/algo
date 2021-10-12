__author__ = 'tanchao@github'

def sample():
    pass

def solution(A, K):
    n = len(A)
    for i in xrange(n - 1):
        print i, "===", A[i], A[i + 1]
        if A[i] == A[i + 1] or A[i] + 1 == A[i + 1]:
            return False
    if not (A[0] == 1 and A[n - 1] == K):  # must both match
        return False
    else:
        return True

if __name__ == '__main__':
    print solution([1,2,3,4,4,3], 3)
    print solution([1, 1, 2, 3, 3], 3)

