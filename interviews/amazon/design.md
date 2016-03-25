# experience
问OOP的时候要多跟面试官交流。问清楚各种假设和功能要求。而且OOP Design很有可能 不要写大部分细节代码只要跟面试官讨论下接口和具体框架
明白各种design的优缺点就可以。

cc150 all design sections

# questions
[] design an elevator
[] OOP Design关于class schedule
[] 关于lastest 3 view Items by customer
[] 解析表达 式,例如“1*2 + 3”,关键要用面向对象的思想设计。需要可以拓展,支持括号,支持开方之类的。
[] 聊现在工作做的系统,设计一个系统,支持各种报表。
[] ParkingLot
[] 设计一个机场调度系统,和面试官多交流有哪些实体需要抽象吧,要想清楚业务流程里的参与者和用例,还有之后的耦合内聚怎么优化等等。
[] 工厂模式,依赖注入
[] LRU Cache,在扩展到集群,用Hash映射解决数据分布。
[] Celebrity problem,当时用图论做的,到后来没来得及做出用栈解决的最优解
[] 一个电话本的例子 http://www.cs.gordon.edu/courses/cs211/AddressBookExample/
[] 用C#写的堪称教科书一般的Blackjack游戏 http://www.codeproject.com/Articles/3121/Blackjack-a-real-world-OOD-example
[] xml文件读取算法
[] OOD (Tic-tac Game) Followups。答:CC150
[] design pattern
[] 设计一个truck tracking system,要求实现查询truck的地点,每天的行程之类 的。一开始写了一个truck class,然后在引导下一点一点的增加功能,
然后问了下 database 的table 应该有哪些东西。
[] 从head，一次改一个字母，要求改完仍是一个有意义的词，找path。这轮基本都在谈思路，感觉不是很好，我用BFS的。
[] 设计一个System玩21点。可以有AI和有人玩。
[] 设计一个FC仓库。要求有车，有一个dock用来卸货，有一个FC有好多dock，有一个controller控制车去哪个dock卸货。
[] 设计一个安装包判断。
[] 设计一个cache。
[] 图书推荐系统，类似facebook, twitter那样的好友系统，可以看评价，可以写评价，有好友列表一类的。CC150有我记得。
[] 设计一个twitter
[] 一个set里面装的是很多job, 每个job有开始的时间和结束的时间。现在需要分配这一堆job给 尽可能少的machine, 
要求是每一个machine在同一个时间段只能做一个job,问怎么让 machine数量最少。
我用了bruth force的方法,in worst case, time complexity is O(n ^ 2), 当讨论怎么降到 O(n)的时候,没时间了。
[] 设计一个邮件系统
[] 用expression tree表达算式,问怎么设计这个数据结构。我说有两个方法:计算这棵树和生成这棵树。先实现了计算的方 法,问有哪些边界情况,
并演示代码运行过程。要实现生成方法时面试官主动降低难度,用 逆波兰式,立即变成leetcode题变种,不过我写到一半时间不够了,
面试官问有哪些边界情况怎么处理就结束了。
还有因为我在代码中写了异常处理,面试官就问runtime exception和普通异常的区别
[] OOD题,设计在线订披萨里的披萨。有各种大小的披萨,披萨可以有各种 topping,同一种topping也可以同时上好几个,比如double cheese。
写披萨的数据结构,然后写个函数计算披萨价格。
[] 一个仓库里有很多items分散在各处,每个item有一个时间(派人去取回它的时间),给你一组要取的items,一组人,
问怎么把items分配到这些人能得到最优的总时间



