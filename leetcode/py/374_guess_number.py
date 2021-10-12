# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
class Solution:
    def guessNumber(self, n: int) -> int:
        if n < 1: return 0 # unexpected
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2 # mid number
            is_picked = guess(mid)
            if is_picked == 0:
                return mid
            elif is_picked == -1:
                right = mid - 1
            elif is_picked == 1:
                left = mid + 1
            else:
                break # unexpected        
        return 0 # unexpected