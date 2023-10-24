"""
739. Daily Temperatures
Solved
Medium
Topics
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # intialize result with zero values as an array equal to the len temp
        result = [0]*len(temperatures)
        stack= []

        for  idx,num in enumerate(temperatures):
            # compare the temparature with the top stack temprature if its greater 
            # enter the loop and pop the number and update the result index with 
            # that value and keep looping unill the stack becomes empty or the 
            # top value in the stack is greater than the currnet temprature 
            while stack and  num > stack[-1][1]:
                index , number = stack.pop()
                result[index] = idx - index
            # add the current temprature to the stack
            stack.append((idx, num))
        return result
