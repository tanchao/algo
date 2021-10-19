NUMBER_TO_LETTER = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


class Solution:
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []
        all_combinations = ['']
        for digit in digits:
            if digit not in NUMBER_TO_LETTER:
                return [] # @todo: unexpected
            curr_combinations = []
            for letter in NUMBER_TO_LETTER[digit]:
                for combination in all_combinations:
                    curr_combinations.append(combination + letter)
            all_combinations = curr_combinations
        return all_combinations


solution = Solution()
print(solution.letterCombinations("42"))