""" 621. Task Scheduler

https://leetcode.com/problems/task-scheduler/description/

youtube link : https://www.youtube.com/watch?v=Z2Plc8o1ld4
               https://www.youtube.com/watch?v=l6-y7MrHLB8
               https://www.youtube.com/watch?v=s8p8ukTyA2I&t=1s


Medium

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
Tasks could be done in any order. Each task is done in one unit of time. 
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), 
that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100]. """


from collections import deque
import heapq
from typing import Counter, List
import time
from memory_profiler import profile

class Leet_621_TaskScheduler:
    #@profile
    def leastInterval(self, tasks: List[str], n: int) -> int:  # complex to understand, require understanding of Heap and deque.
        # each task 1 unit time
        # minmize idle time
        count = Counter(tasks)  # This will creat a dictonary with key value pair, meaning Task and it's frequency . Example {'A':3, 'B': 3}, length is 2
    
        maxHeap = [-cnt for cnt in count.values()]  # this will create an array with negative number [-3, -3]
        #print("The created heap is : ", end="")
        #print(maxHeap) 
        heapq.heapify(maxHeap)
        #print("The created heap is : ", end="")
        #print(maxHeap) 
        time = 0
        q = deque() # pairs of [-cnt, idleTime]
        #print("deque : ", end="")
        #print(q) 

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                #print("cnt : ", end="")
                #print(cnt)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
    

    #@profile
    def leastInterval_1(self, tasks: List[str], n: int) -> int:
        # define a frequency dictonary to have task and its frequency count
        print ("")
        print ("Tasks = ",tasks)
        print ("Cool Down period which is n (n = ideal time between the task) =", n)
        tasklength = len(tasks)
        if n == 0:
            return tasklength
        #freq = {}
        #for task in tasks:
        #    if task not in freq:
        #        freq[task] = 1
        #    else:
        #        freq[task] += 1

        freq = Counter(tasks)   # this is one liner to save time and extra lines as above commented lines
        

        print ("frequency of the each task=", freq)
        
        #print ("freq.items = ", freq.items())
        
        #only_freq = []
        #for value in freq.values():
        #    only_freq.append(value)

        only_freq = [value for key, value in freq.items()]
        #only_freq = [cnt for cnt in freq.values()]

        print ("frequency count of each task in a array list = ", only_freq)
        #print ("frequency count of each task=", freq)
        max_freq = max(only_freq)
        print ("max_freq (Highest frequency count of the task) = ", max_freq)
        
        max_freq_tasks_groups = only_freq.count(max_freq) # find the Count of tasks has the max frequency.
        print ("max_freq_tasks_groups (Highest frequency task) = ", max_freq_tasks_groups)
        
        
        # formula is as below
        # least task time = total group * items in a group +  task count with higest frequency
        # [["A","A","A","B","B","B","B"], 2
        # [B A _, B A _, B A _, B] total 3 groups and each group has 3 elelments + highest task count with higest frequency
        # least task time = (max frequency of the task - 1) * (ideal cycle count, + 1) +  task count with higest frequency
        # ["A","A","A","B","B","B"], 2
        # [B A _, B A _, B A] total 3 groups and each group has 3 elelments + highest task count with higest frequency
        # least task time = total group * items or elements  in the group +  task count with higest frequency
        # least task time = (highest frequency - 1) * ( n + 1) +  number of task with higest frequency

        print ("leasttasktime = (max_freq - 1) * (n + 1) + max_freq_tasks")
        leasttasktime = (max_freq - 1) * (n + 1) + max_freq_tasks_groups
        print ("leasttasktime:", leasttasktime)
        print ("tasklength:", tasklength)
        return max(tasklength, leasttasktime)
    

    def leastInterval_greedy_algorithm(self, tasks: List[str], n: int) -> int:
        # define a frequency dictonary to have task and its frequency count
        print ("")
        print ("Tasks = ",tasks)
        print ("Cool Down period which is n (n = ideal time between the task) =", n)
        tasklength = len(tasks)
        if n == 0:
            return tasklength
        """ freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1 """
        freq = Counter(tasks)   # this is one liner to save time and extra lines as above commented lines
        print ("frequency of the each task=", freq)
        """ only_freq = []
        for value in freq.values():
            only_freq.append(value) """
        
        only_freq = [value for key, value in freq.items()] 
        only_freq.sort(reverse=True) # as we have to remove frequency used to calculate the Max CPU Idle time
        print ("frequency count of each task in a array list = ", only_freq)
        max_freq = max(only_freq) 
        print ("max_freq (Highest frequency count of the task) = ", max_freq)
        MaxcpuIdleTime = (max_freq - 1) * n
        print ("CPU idle time with the start of processing = ", MaxcpuIdleTime)
        for i, freq in enumerate(only_freq):
            if i == 0:
                continue
            MaxcpuIdleTime -= min(max_freq - 1, only_freq[i])
        print ("CPU idle time after processing the tasks = ", MaxcpuIdleTime)
        return max(tasklength, tasklength+MaxcpuIdleTime) # max of two value is required as if the cpu idle time goes below length of the task, which is wrong.
        #return tasklength+MaxcpuIdleTime   # This will fail certain test cases.


if __name__=="__main__":
    leet_621 = Leet_621_TaskScheduler()
    print (leet_621.leastInterval(["A","A","A","B","B","B"], 2))
    print (leet_621.leastInterval(["A","A","A","B","B","B","B"], 2))
    print (leet_621.leastInterval(["A","A","A","B","B","B"], 0))
    print (leet_621.leastInterval(["A","A","A","B","B","B","C","C","C","D","D","E"], 2))
    print (leet_621.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
    print (leet_621.leastInterval(["A","B","A","B","A","B"], 2))
    
    print ("================================================================================")
    print (leet_621.leastInterval_1(["A","A","A","B","B","B"], 2))
    print (leet_621.leastInterval_1(["A","A","A","B","B","B","B"], 2))
    print (leet_621.leastInterval_1(["A","A","A","B","B","B"], 0))
    print (leet_621.leastInterval_1(["A","A","A","B","B","B","C","C","C","D","D","E"], 2))
    print (leet_621.leastInterval_1(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
    print (leet_621.leastInterval_1(["A","B","A","B","A","B"], 2))

    print ("======================================================================================")
    print (leet_621.leastInterval_greedy_algorithm(["A","A","A","B","B","B"], 2))
    print (leet_621.leastInterval_greedy_algorithm(["A","A","A","B","B","B","B"], 2))
    print (leet_621.leastInterval_greedy_algorithm(["A","A","A","B","B","B"], 0))
    print (leet_621.leastInterval_greedy_algorithm(["A","A","A","B","B","B","C","C","C","D","D", "E"], 2))
    print (leet_621.leastInterval_greedy_algorithm(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
    print (leet_621.leastInterval_greedy_algorithm(["A","B","A","B","A","B"], 2))
        
