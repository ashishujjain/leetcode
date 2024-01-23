""" 
207. Course Schedule || https://leetcode.com/problems/course-schedule/description/
Youtube:    
    https://www.youtube.com/watch?v=EgI5nU9etnU
    https://www.youtube.com/watch?v=qe_pQCh09yU&list=RDQMLViDeLZ71KI&start_radio=1

Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.

Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique. 


ALgorithm:
1. Define a preRequisitesMap to store the prerequisites example:  {0: [], 1: []}
2. use loop to update the preRequisitesMap with the mapping of course to dependency 
        example:  {0: [], 1: [0]}
    a. in the prerequisites [[1, 0]], 1 is dependent on 0
3. define a Set with the name courseVisitSet
4. defins a DFS (depth First Search method for traversing the linkedlist)
    a. 


"""

from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq List
        print (f"prerequisites : {prerequisites } and numCourses : {numCourses}")
        print ("")
        preRequisitesMap = { i:[] for i in range(numCourses)}
        print (f"preRequisitesMap with empty list : {preRequisitesMap}")
        print ("")
        for courses, preRequisites in prerequisites:
            preRequisitesMap[courses].append(preRequisites)
            #print (f"Enter the course {courses} and it's preRequisites {preRequisites} to preRequisitesMap {preRequisitesMap}")
        print (f"course to it's preRequisites in preRequisitesMap : {preRequisitesMap }")
        print ("")
        output = []
        #VisitSet = all courses along the curr DFS path
        courseVisitSet =  set()  #Set in Python programming is an unordered collection data type that is iterable, mutable and has no duplicate elements. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.
        print (f"Setting the set with name {courseVisitSet}")
        print ("")
        def dfs(course): # Depth First Search to check the DAG (Directed acyclic graph)
            print (f"   Entering the DFS function for the course {course}")
            if course in courseVisitSet: 
                print (f"   course {course} is in courseVisitSet {courseVisitSet}, returning False")
                print ("")
                return False # this case means that it's not a DAG, we are in cyclic loop
            if preRequisitesMap[course] == []:
                print (f"   There is no preRequisites for the course {course}, in preRequisitesMap {preRequisitesMap}, returning True")
                print ("")
                return True  # this case means that this is a DAG
            courseVisitSet.add(course) # we are visiting the course add the entry to courseVisitSet and check via DFS
            print (f"   course {course} added in courseVisitSet {courseVisitSet}")
            for pre in preRequisitesMap[course]: # recursively run the DFS on course preRequisites
                print (f"       Running DFS on prerequisite {pre} in preRequisitesMap {preRequisitesMap[course]}")
                callingDfs = dfs(pre)
                print (f"       Running DFS on {course} preRequisites {pre} in the preRequisitesMap  {preRequisitesMap}")
                if not callingDfs:#Cheking the return of DFS
                    print (f"       Cheking the course {course} preRequisites {pre} in the preRequisitesMap {preRequisitesMap} for empty list, since it's not empty, returning False") 
                    return False
            courseVisitSet.remove(course) # This means course can be visited, hence remove form courseVisitSet
            print (f"   course {course} removed in courseVisitSet {courseVisitSet}")
            preRequisitesMap[course] = [] # If course is visited and can be completed, it need to be update in the preRequisitesMap as empty list
            print (f"   Set the course {course} as empty list in preRequisitesMap {preRequisitesMap}")
            output.append(course)
            return True
        
        for course in range(numCourses): #iterate over the numcourses (total number of course)
            print ("")
            print (f"Running DFS on {course}")
            callingDfsCOurse = dfs(course)
            print (f"Running DFS on {course} and it's return is {callingDfsCOurse}")
            if not callingDfsCOurse: #if dfs is False with not it returns False, so final return is False
                print (f"DFS on course : {course} is returning False") 
                return False
        #print ("output = ", output)
        return True #Overall return is True

if __name__=="__main__":
    leet_207 = Solution()
    prerequisites = [[1,0]]
    numCourses = 2
    print (leet_207.canFinish(numCourses, prerequisites))
    print ("")
    print ("=================================================")
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    numCourses = 4
    print (leet_207.canFinish(numCourses, prerequisites))
    print ("")
    print ("=================================================")
    prerequisites = []
    numCourses = 1
    print (leet_207.canFinish(numCourses, prerequisites))
    print ("")
    print ("=================================================")
    prerequisites = [[1,0],[0,1]]
    numCourses = 2
    print (leet_207.canFinish(numCourses, prerequisites))
    print ("")
    print ("=================================================")
    prerequisites = [[0,1],[0,2],[1,3],[1,4],[3,4]]
    numCourses = 5
    print (leet_207.canFinish(numCourses, prerequisites))
    print ("")
    print ("=================================================")
    prerequisites = [[0,1],[0,2],[1,3],[1,4],[3,4],[4,1]]
    numCourses = 5
    print (leet_207.canFinish(numCourses, prerequisites))