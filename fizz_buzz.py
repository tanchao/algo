'''
CodeEval.com > Easy Challenges > Fizz Buzz

Input sample:
3 5 10
2 7 15

Output sample:
1 2 F 4 B F 7 8 F B
1 F 3 F 5 F B F 9 F 11 F 13 FB 15

@author tanchao@github
'''

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # ignore test if it is an empty line
    test = test.strip()
    if test == '': continue
    params = test.split(' ')
    if len(params) == 3:
        fizz, buzz, count = int(params[0]), int(params[1]), int(params[2])
        output_ = ''
        for num in range(1, count + 1):
            if (num % fizz != 0) and (num % buzz != 0): output_ += str(num)
            else:
                if num % fizz == 0: output_ += 'F'
                if num % buzz == 0: output_ += 'B'
            output_ += ' '
        print output_.rstrip()
    else:
        print 'error input params'

test_cases.close()
