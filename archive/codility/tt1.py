__author__ = 'tanchao@github'


def sample(X, A):
    left, right = 0, len(A) - 1
    count = 0
    while left < right:
        while left < right and A[left] != X:
            left += 1  # move right
        left += 1
        count += 1
        while left < right and A[right] == X:
            right -= 1  # move left
        right -= 1
        count -= 1
        if count == 0 and left >= right:
            if left == 1 and right == 0:  # all X elements
                left = 0
            break  # meet
    return left


if __name__ == '__main__':
    print sample(5, [5,5,1,7,2,3])
    print sample(5, [5,5,1,7,2,3,5])
    print sample(5, [5,5,5,5,5])
    print sample(5, [1,1,1,2,5])
    print sample(5, [1,1,1,2])
