#
# @lc app=leetcode id=1689 lang=python3
#
# [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
#

# @lc code=start
class Solution:
    def minPartitions(self, n: str) -> int:
        # this question the answer is written in the hint
        # work on single digit first
        # for multiple digit, work on each digit independently and sum up
        # hence the steps required is the max in that digit
        n  = list(n)
        return int(max(n))   
# @lc code=end

