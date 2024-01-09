""" Leet_1834_SingleThreadedCPU
Youtube: https://www.youtube.com/watch?v=RR1n-d4oYqE

Medium

Hint
You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.

 

Example 1:

Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.
Example 2:

Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]
Explanation: The events go as follows:
- At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
- At time = 40, the CPU finishes task 1 and becomes idle. """


import heapq
from typing import List


class Leet_1834_SingleThreadedCPU:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        taskLength = len(tasks)
        tasks = [[enqueueTime, processingTime, taskIndex] for taskIndex, [enqueueTime, processingTime] in enumerate(tasks)]
        tasks.sort() # sorting the task list on the enqueueTime in each index
        #print ("tasks : ", tasks)
        curTime = pointerforTask = 0 # Pointing to the next available task and CurreTime as 0
        ansIndex, priorityQueue = [], []
        while pointerforTask < taskLength or priorityQueue:
            # if there is no task in the queue and curTime < next available task
            if not priorityQueue and pointerforTask < taskLength and curTime < tasks[pointerforTask][0]:
                curTime = tasks[pointerforTask][0]
            # add available tasks before curTime to the priorityQueuq
            while pointerforTask < taskLength and tasks[pointerforTask][0] <= curTime:
                heapq.heappush(priorityQueue, [tasks[pointerforTask][1], tasks[pointerforTask][2]])
                pointerforTask += 1
            # pick next task to process
            processingTime, taskIndex = heapq.heappop(priorityQueue)
            ansIndex.append(taskIndex)
            curTime += processingTime
        return ansIndex
    
    def getOrder_neetcode(self, tasks: List[List[int]]) -> List[int]:
        taskLength = len(tasks)
        for taskIndex, eachtask in enumerate(tasks):
            eachtask.append(taskIndex)
        #tasks.sort(key = lambda t : t [0]) # sorting the task list on the enqueueTime in each index
        tasks.sort()
        #print (tasks)
        ansIndex, priorityQueue = [], []
        pointerforTask, curTime = 0, tasks[0][0]
        
        while priorityQueue or pointerforTask < taskLength:
            while pointerforTask < taskLength and curTime >= tasks[pointerforTask][0]:
                heapq.heappush(priorityQueue, [tasks[pointerforTask][1], tasks[pointerforTask][2]])
                pointerforTask += 1

            if not priorityQueue:
                curTime = tasks[pointerforTask][0]
            else:
                processingTime, taskIndex = heapq.heappop(priorityQueue)
                curTime += processingTime
                ansIndex.append(taskIndex)
        return ansIndex



if __name__=="__main__":
    leet_1834 = Leet_1834_SingleThreadedCPU()

    tasks = [[1,2],[2,4],[3,2],[4,1]]
    Output = [0,2,3,1]
    #tasks = [[3,2],[1,2],[2,4],[4,1]]
    result = leet_1834.getOrder(tasks)
    print ("Given Task Order:" ,tasks)
    if result == Output:
        print ("OutPut getOrder:" ,result)
    
    result = leet_1834.getOrder_neetcode(tasks)
    if result == Output:
        print ("OutPut getOrder_neetcode:" ,result)

    print ("")
    tasks = [[3,2],[1,2],[2,4],[4,1]]
    Output = [1, 0, 3, 2]
    result = leet_1834.getOrder(tasks)
    print ("Given Task Order:" ,tasks)
    if result == Output:
        print ("OutPut getOrder:" ,result)
    
    result = leet_1834.getOrder_neetcode(tasks)
    if result == Output:
        print ("OutPut getOrder_neetcode:" ,result)
    print ("")

    tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
    Output = [4,3,2,0,1]
    result = leet_1834.getOrder(tasks)
    if result == Output:
        print ("OutPut getOrder:" ,result)
    
    result = leet_1834.getOrder_neetcode(tasks)
    if result == Output:
        print ("OutPut getOrder_neetcode:" ,result)

    print ("")
    
    tasks = [[1,2],[10,4],[14,2],[14,1]]
    Output = [0,1,3,2]
    result = leet_1834.getOrder(tasks)
    print ("Given Task Order:" ,tasks)
    if result == Output:
        print ("OutPut getOrder:" ,result)
    
    result = leet_1834.getOrder_neetcode(tasks)
    if result == Output:
        print ("OutPut getOrder_neetcode:" ,result)