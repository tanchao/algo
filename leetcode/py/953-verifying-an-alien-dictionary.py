#7:10
# override String.compareTo()
class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        if words is None: return False # @todo: unexpected
        if words is not None and len(words) <= 1: return True # treat empty as sorted
        for i in range(len(words) - 1):
            if not self.compare(order, words[i], words[i+1]):
                return False
        return True
    
    # return True if @first should be sorted ahead of @second in @order
    def compare(self, order: str, first: str, second: str) -> bool:
        cursor = 0
        while (cursor < len(first) and cursor < len(second)):
            first_index = order.index(first[cursor])
            second_index = order.index(second[cursor])
            if first_index > second_index:
                return False
            elif first_index < second_index:
                return True
            else: # equals
                cursor += 1
        if len(second) < len(first): # means @second is shorter than @first
            return False
        return True

solution = Solution()
print(solution.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
