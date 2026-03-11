#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        
        for i, v in enumerate(nums):
            if (target - v in seen_dict) == False:
                seen_dict[v] = i
            else:
                return [i, seen_dict[target-v]]
        
# @lc code=end

