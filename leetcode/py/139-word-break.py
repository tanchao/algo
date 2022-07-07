# first revision by myself, not working, check discussion then
import collections


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        queue, visited = collections.deque(), set()
        queue.appendleft(0)
        visited.add(0)
        while len(queue) > 0:
            curr = queue.pop()
            for i in range(curr, len(s) + 1):
                if i in visited: 
                    continue
                if s[curr:i] in wordDict:
                    if i == len(s):
                        return True
                    queue.appendleft(i)
                    visited.add(i)
        return False
            
solution = Solution()
print(solution.wordBreak("cars", ["car","ca","rs"]))