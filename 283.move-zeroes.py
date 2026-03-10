#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        
        if len(nums) == 1 or sum(nums) == 0:
            return nums
        
        while i < j:
            if nums[i] == 0:
                while nums[j] == 0:
                    j -= 1
        
# @lc code=end

