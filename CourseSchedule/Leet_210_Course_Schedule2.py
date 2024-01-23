""" 
https://leetcode.com/problems/course-schedule-ii/description/

Youtube: 
                    https://www.youtube.com/watch?v=Akt3glAwyfY
Topological sort    https://www.youtube.com/watch?v=qe_pQCh09yU&list=RDQMLViDeLZ71KI&start_radio=1

210. Course Schedule II
Medium

Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: [0,1]
    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
    Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3]
    Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
    So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
    Input: numCourses = 1, prerequisites = []
    Output: [0]
 

Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= numCourses * (numCourses - 1)
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    ai != bi
    All the pairs [ai, bi] are distinct.
"""

from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # map each course to prereq List
        print (f"prerequisites : {prerequisites } and numCourses : {numCourses}")
        print ("")
        preRequisitesMap = { c:[] for c in range(numCourses)}
        print (f"preRequisitesMap with empty list : {preRequisitesMap }")
        print ("")
        for courses, preRequisites in prerequisites:
            preRequisitesMap[courses].append(preRequisites)
        # a course has 3 possible states:
        # Visited - > course has been added to output
        # Visiting - > Course not added to output, but added to cycle
        # unvisited - > course not added to output or cycle
        
        print (f"course to it's preRequisites in preRequisitesMap : {preRequisitesMap }")
        print ("")
        output = []
        courseVisitSet, cycle =  set(), set()  
        print (f"Setting the set with name {courseVisitSet}")
        print ("")
        def dfs(course): # Depth First Search to check the DAG (Directed acyclic graph)
            print (f"   Entering the DFS function for the course {course}")
            print ("")
            if course in cycle: 
                print (f"   course {course} is in cycle {cycle}, returning False")
                print ("")
                return False
            if course in courseVisitSet: 
                print (f"   course {course} is in courseVisitSet {courseVisitSet}, returning True")
                print ("")
                return True # this case means that it's not a DAG, we are in cyclic loop
            cycle.add(course)
            print (f"   course {course} is added to cycle {cycle}")
            print ("")
            for pre in preRequisitesMap[course]: # recursively run the DFS on course preRequisites
                print (f"       Running DFS on course {course} prerequisite={pre} in preRequisitesMap[{course}]={preRequisitesMap[course]}, full preRequisitesMap={preRequisitesMap}")
                callingDfs = dfs(pre)
                if callingDfs == False:#Cheking the return of DFS
                    print (f"       Cheking the course {course} preRequisites {pre} in the preRequisitesMap {preRequisitesMap} for empty list, since it's not empty, returning False") 
                    return False
            cycle.remove(course)
            print (f"   course {course} is removed from cycle {cycle}")
            courseVisitSet.add(course) # we are visiting the course add the entry to courseVisitSet and check via DFS
            print (f"   course {course} is added to courseVisitSet {courseVisitSet}")
            output.append(course)
            print (f"   course {course} is added to output {output}")
            print ("")
            return True
        
        for course in range(numCourses): #iterate over the numcourses (total number of course)
            print ("")
            print (f"Running DFS on {course}")
            callingDfsCOurse = dfs(course)
            print (f"Running DFS on {course} and it's return is {callingDfsCOurse}")
            if callingDfsCOurse == False: #if dfs is False with not it returns False, so final return is False
                print (f"DFS on course : {course} is returning False, returning empty List") 
                return [] # return empty list
        return output #return the array

if __name__=="__main__":
    leet = Solution()
    prerequisites = [[1,0]]
    numCourses = 2
    print (leet.findOrder(numCourses, prerequisites))
    print ("")
    print ("=================================================")
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    numCourses = 4
    print (leet.findOrder(numCourses, prerequisites))
    print ("")
    print ("=================================================")
    prerequisites = []
    numCourses = 1
    print (leet.findOrder(numCourses, prerequisites))
    print ("")
    print ("=================================================")
    prerequisites = [[1,0],[0,1]]
    numCourses = 2
    print (leet.findOrder(numCourses, prerequisites))
    print ("")
    print ("=================================================")
    prerequisites = [[0,1],[0,2],[1,3],[1,4],[3,4]]
    numCourses = 5
    print (leet.findOrder(numCourses, prerequisites))
    print ("")
    print ("=================================================")
    prerequisites = [[0,1],[0,2],[1,3],[1,4],[3,4],[4,1]]
    numCourses = 5
    print (leet.findOrder(numCourses, prerequisites))
    print ("")
    print ("=================================================")
    prerequisites = [[0,1],[0,2],[1,3],[3,2],[4,0],[5,0]]
    numCourses = 6
    print (leet.findOrder(numCourses, prerequisites))