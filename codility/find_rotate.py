def find(A, target):
    len_a = len(A)
    if len_a < 1:
        return False
    if len_a == 1:
        return A[0] == target
    left, right = 0, len_a - 1
    while left < right:
        mid = left + (right - left) / 2
        print left, mid, right, A[left], A[mid], A[right]
        if target == A[mid] or target == A[left] or target == A[right]:
            return True  # mid/left/right is the index
        if target < A[mid]:
            if target > A[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target < A[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False


def find_dup(A, target):
    len_a = len(A)
    if len_a < 1:
        return False
    if len_a == 1:
        return A[0] == target
    left, right = 0, len_a - 1
    while left < right:
        mid = left + (right - left) / 2
        # print left, mid, right, A[left], A[mid], A[right]
        if target == A[mid] or target == A[left] or target == A[right]:
            return True  # mid/left/right is the index
        if A[mid] > A[left]:  # left-mid is sorted
            if A[left] < target < A[mid]:  # target between left and mid
                right = mid - 1
            else:
                left = mid + 1
        else:  # mid-right is sorted
            if A[mid] < target < A[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False


if __name__ == '__main__':
    s = raw_input('pls enter array: \n')
    t = int(raw_input('pls enter target: \n'))
    a = map(int, s.split())
    print a, t
    print find_dup(a, t)