#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ops in operations:
            if ops == '+':
                if len(stack) >= 2:
                    stack.append(stack[-1] + stack[-2]) 
                else:
                    stack.append(stack[-1])
            elif ops == 'C':
                stack.pop()
            elif ops == 'D':
                if stack:
                    stack.append(2 * int(stack[-1]))
            else:
                stack.append(int(ops))
        
        return sum(stack)
                
                

        
# @lc code=end

