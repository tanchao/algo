# experience
算法题最好先讲出方法,各种边界条件最好问,最后基本都会问到给出test case测试你的代码。

CC150

# questions
[] letter combination
[] graphic bfs/dfs travel
[] inplace sort, big array append small array (compare from tail)
[] Largest K element
[] 将已经有序的N个ArrayList merge 为一个有序的List,LC原题,做完后因为其中用到了Heap,让顺便实现了一下Heap的插入,中间卡壳了一下,
想到Heap可以用数组表示后,才顺利解决。
[] 对一个无序数组,判断它是否是连续序列,其中0是magic number
[] 给定阿拉伯数字的串,要求输出它的中文表示,例如:9909 -》 九千九百零九,其中阿拉伯数字最长8位(边界条件判断,测试用例first)
[] 给两个列表,每个列表装着一样的元素,合并两个列表,并要求短的列表的元素把长列表元素尽可能均衡分开。比如列表为AAAAA和BBBBBB,
返回BABABABABAB;又比如 AAAAAA和BBBB,返回AABABABABA。
[] 实现heap
[] 堆栈结构
[] 给你一个API,input是一个城市,输出是邻近城市,问实现一个方法,判断 两个城市之间是否可以到达。答:BFS
[] 继续上问,实现一个方法,找出两个城市之间所有的路径。答:DFS
[] 继续上问,如果client有很多特殊请求(如不想经过城市A,不想途转太多城市)怎么办?答:Strategy Design Pattern
[] isValidBST()。答:LeetCode
[] HashTable出现很多collision怎么办?答:(Rehashing)load factor。
[] 给你一个dictionary(all English word)和一个一维的character数组 (duplicated),找出所有可以用数组表示的字典里的单词。
答:遍历字典,判断是否能被表示
[] 给一个array 找出里面出现奇数次的数字。 (XOR)
[] linkedlist 每个节点多一个random pointer,问怎么复制,hashmap,很简单, 没让写代码。
[] 给一个平方数,求平方根。就/2 /2 /2。。。 log(n)的复杂度
[] 问了个循环列表,删除指定节点,写完让想一些edge case 测试一下代码正确性
[] 第一轮，binary tree里给个node，找出比他大的下一个node。
[] 给一串没空格的字符串，判断是不是一句话，之后会叫你返回加上空格后的那句话。
[] 给一个int的array，值代表高度。求这个东西能储存多少水。
[] 给你一个函数返回所有amazon有的Product，还有一个函数返回amazon仓库里面的所有Product记录。用这两个函数找出特定要求的货物。
[] 无限输入流找中位数,follow up,如果memory非常小怎么办。(average)
[] merge k list, bruce force的方法,然后问了时间复杂度和空间复杂度。min heap, 然后写了除了constructor以外,所有min heap的构建方法。
最后问了问heap的内部机制 
[] two sum in sorted list 先讲了用hashmap, 然后用binary search。follow up问了一下如果有duplicate 怎么办
[] stack + min stack
先问了stack的pop, push, peek的时间复杂度。写了stack类的pop, push 和 peek方法。然 后让在自己设计的stack类的基础上实现min stack
[] 重写一个HashMap,多加一个功能,可以按照insert的顺序输出出来
[] 给一个矩阵,连通的非0元素组成一个island,问这个矩阵里island的数量.
[] Word Ladder,介于1和2中间吧,只需要输出最短的一条路径就可以
[] 一个排好序的整数数组,返回所有的range. 比如1,2,3,5,7,8,10返回[1,3],[5,5],[7,8],[10,10]
[] find lowest common ancester. 最开始假设有parent, 然后没有parent的话怎么做,我说了一个top down approach,然后他说要优化,
然后我说 了botom up,最后实现bottom up的代码。期间每种都要比较复杂度。
[] 然后让实现一个interface 实现两个功 能: 一个是能够check input的单词拼写有没有错误 二是可以给你alternative words。
[] 第二个是binary tree找到距离最长的两个leaf nodes包含的nodes个数。
[] 




