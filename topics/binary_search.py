'''
1. core is find the mid number, note the floor division
2. edge is handle the mid movement (+1, -1)
3. comparator is generic
'''

def find_target(self, n: int, target: int) -> int:
    if n < 1: return 0 # unexpected
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2 # mid number
        is_picked = self.compare(mid, target)
        if is_picked == 0:
            return mid
        elif is_picked == -1:
            right = mid - 1
        elif is_picked == 1:
            left = mid + 1
        else:
            break # unexpected        
    return 0 # unexpected

def compare(self, mid: int, target: int) -> int:
    if mid == target:
        return 0
    if mid < target:
        return -1
    if mid > target:
        return 1