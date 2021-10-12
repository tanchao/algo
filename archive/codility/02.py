__author__ = 'tanchao@github'

def solution(A):
    len_a = len(A)
    if len_a <= 1:  # special case
        return 0
    A.sort()
    cur_count, result = 1, 1
    count_list = []
    cur = A[0]
    for i in xrange(1, len_a):
        if cur == A[i]:
            cur_count += 1
        else:
            count_list.append(cur_count)  # store last counts
            if A[i] > cur + 1:  # break as A[i] > cur + 1
                count_list.append(0)
            cur_count = 1
            cur = A[i]
    count_list.append(cur_count)
    if len(count_list) == 1:
        result = count_list[0]
    else:
        for j in xrange(len(count_list) - 1):
            if count_list[j] + count_list[j + 1] > result:
                result = count_list[j] + count_list[j + 1]
    if result == 1:
        result = 0  # amplitude = 0 when single element
    return result

if __name__ == '__main__':
    # print solution([2, 3, 5, 7, 8, 11, 0, -1, -1, 9])
    print solution([2147483646, 2147483646])
    # print solution([-2147483646, -2147483646, 2147483647, 2147483647])
    # print solution([-2147483648, -2147483648, -2147483647, -2147483647, -2147483646])
