# TODOs

- [x] <0124> Re-phase answers with more objective and match-oriented
- [] <0131> Read and prepare more about Big-Data platform: Hadoop (Lucene), Spark, Pig etc.

# prerecord

- [x] Could we have your name and the reason why you are interested in Rakuten?

> Hello Rakuten, my name is Tan Chao, nice to meet you.

> Rakuten's business has been doing real good staffs for people, it served and changed people's life style 
significantly; Rakuten has proved its value in Japan, and now is expanding it's value worldwide, I can't agree more about
this value and I want to be part of it; About this position, Big-Data platform is a wonderland for every software engineer to 
make magic happen, which is so attractive to me too; Meanwhile, me and my family are willing to explore different cultures, 
Tokyo is definitely one of the most dynamic cities in Asia. With all these matches, I am here for Rakuten. Thank you.

- [x] Please tell us your technical background and how you will be able to contribute to the success of the company.
If you already have work experience, please share that as well.

> I graduated from East China University of Science and Technology in 2008, with a Bachelor degree of Computer Science and Diploma of Finance . 
I have been worked as a developer since then, proficient programming in Python and Java, skilled in rational database and 
SQL, hands on stored procedure and some basic db tuning, I am quite familiar with front-end technologies, such as HTML/CSS/JS etc. 
I am interested in Open Source Software, like Node.js, Go-lang, also I practiced some Big-Data platform, such as Spark, Hadoop.
I worked in finance and e-commence industry in last 7 years, located in SG/USA/HK for a while, 
right now a Senior Software Engineer in HSBC GZ, I am responsible for leading a global dev team for internal platform design
and code and also some other business projects. We used Python and JavaScript a lot, also we used GeneOS and Spark to monitor and 
invest our data. 
From the job description and company's information, I believe my 
experience and background can help me adopt into the Rakunten's global environment very quickly, once I get into the team, 
I can add value to the team and the firm. Thank you.

- [x] What is your greatest strength and how you leverage your strength for peak performance? Please give us an example.

> Confidence! I believe in myself, for my smartness, my intelligence, which makes me learn faster and start quicker. e.g.
When I joint HSBC about 4 yrs ago, I had to start with a new programming language-Python and a new working environment- 
UNIX. However I managed to build the MESA project from scratch within 3 months. Right now this MESA framework has been 
well recognized among the department, used by 3 systems on 3 sites, globally.I had my way to pick up a technical skills 
quickly, first an official start up tutor, second copy an example project and practice, third read a lovely book with 
details, last not least combine my coding experience with it. In all I have confidence to take responsibilities and 
make it successfully. Thank you.

- [x] *This question is for only those who have worked before* Have you ever changed your job? or are you trying to change
your job? Please tell us why.

> Yes, I worked for 4 companies in my career path. I joint HSBC since 2012, after 4 years engagement and enhancement, 
our project and team are stable now, however I keep looking for self development at this stage. Weeks ago HR contacted me about this 
position and introduced me the exciting team and exciting BIG challenges. As far as I know Rakuten and Big-Data department can give me 
a better growth in career, plus there are big & interesting problems to solve. Also I agreed the organization's value,
believe the future of it. So the reason why I am here is I am trying to seek for better career development and make some
difference. Thank you.  

- [x] What are your career goal and career plans? How does this job fit into your career plans?

> I want to be a solid tech lead till I am old enough, I am willing to lead a team with cutting edge technologies and 
create cool things. I want to bring the robot mind into the work, automate boring stuffs to let people focus on 
interesting stuffs. I am interested in Big-Data tech chain recently, as it shows machine intelligence, and the 
future for world. From my understanding, Rakuten has the gene to introduce technology into the business value, thus they value 
technology the same way. I believe the Big-Data department need efficient ideas and tools to handle the difficult and BIG 
problems, and automation should be a good solution instead of manual work. With these understandings and expectation, it is 
reasonable to start a new journey with Rakuten. And I sincerely wish I can grow with the team, create BIG value with 
the company. Thanks, thank you very much.


# behavior
  - Why do u choose to work in Japan?
  - Why do u choose to Rakuten?
  - Have u joined some project before?
  - Do u familiar with Web knowledge?
  - What's your greatest strength? weakness?
  - Tell me about something on your resume
  - Tell us about a book you've read recently on a technical topic
  - What can you bring to Rakuten?
  
# technical
  - [x] Codility warm up
  - [x] Codility specific questions practice
    - [x] rectangles intersection (refer to rec.inter.py)
    - [x] complementary pairs (refer to complementary.pair.py)
  - Skills
    - Have you ever done unit testing?
    - Have you ever used or known Hadoop, Hive, Pig, Zookeeper, Cassandra, Spark, Kafka?
      - Hadoop
      - Lucene
      - Spark
      - Kafka
      - RabbitMQ
      - Chef
    - Have you worked on managing high performance mission-critical application? Multi-threading? Concurrency?
    - Code review tools, Java /Database related Qs  
    - What data structure will you use to keep top 10 spender for your e-commerce site providing you can keep all records in memory?  
    - Explain a few technical terms like markov chain, singleton, mvc, bloom filter, opportunistic lock, row-level locking  
    
- **experience**
  - [] grad process : http://www.1point3acres.com/bbs/thread-136818-1-1.html
    - [x] 1. 已知 a>0, b>0, a+b<10, 证明ab<25;
    ```
    (a+b)*(a+b)<10*10 => (a-b)(a-b)+4ab<100 => ab<25-(a-b)(a-b)
    ```
    - [x] 2. coding: implement rand7 by using rand5
    ```
    def ran7():
        while True:
            num = (rand5() - 1) * 5 + rand5() - 1
            if 1 <= num <= 21:
                return num % 7 + 1
    ```
    - [x] 3. izip and itertool in python; [itertool ref](http://www.cnblogs.com/cython/articles/2169009.html)
    ```
    from itertools import combinations, izip, imap, repeat 
    ```
    - [x] 4. how to plot x=y in matlab;
    ```
    import numpy as np
    import matplotlib.pyplot as plt
    ```
    - [x] 5.how to generate an integer array form 1 to 1000 in matlab;    
    ```
    ary = [x + 1 for x in xrange(1000)]
    ```
    - [x] 6. how to search all.txt file under the given directory in Linux;
    ```
    cd ~/projects/algo
    ls -ltr interviews/rakuten/*.txt
    find . -name '*.txt'
    ```
    - [x] 7.difference between git pull andgit fetch;
    ```
    git pull will automatically merge local branch;
    git fetch will show merge status first, let user decide;
    ```
    - [x] 8. give at least one new feature for C++;
    ```
    Python 3.5: 
    # a new matrix multiplication operator: a @ b .
    # collections.OrderedDict is now implemented in C, which improves its performance between 4x to 100x times.
    Python 3 VS Python 2:
    # range(), !=, repr(), input() NOT xrange(), <>, ``, raw_input()
    # print(""), not print ""
    # int / int -> float, // -> int
    Java 7:
    Java 8:
    // interface have default implementation
    // function programming friendly
    // lambda
    Collections.sort(names, (String a, String b) -> {
        return b.compareTo(a);
    });
    ```
    - [] 9. what's map reduce;
    - [] 10. tell me about your hadoop experience;
    - [] 11. tell me about your java experience. 
    - [] 12. can you overload constructor in C++, how about destructor?
    - [] 13. tell me your experience in machine learning
    - [] 14. reverse string, analyze time and space complexity;
    - [] 15. find loop in a linked list, time complexity
    