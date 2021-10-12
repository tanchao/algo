class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        count = 0
        print string
        for i in xrange(length - 1, -1, -1):
            count += 1
            print i, count
            if string[i] == ' ':
                string[-count] = '0'
                count += 1
                string[-count] = '2'
                count += 1
                string[-count] = '%'
            else:
                string[-count] = string[i]
        print ''.join(string[-count:])
        return count - 1  # count starts from 1

if __name__ == '__main__':
    s = Solution()
    sl = [x for x in 'Mr John Smith'] + [''] * 50
    s.replaceBlank(sl, 13)