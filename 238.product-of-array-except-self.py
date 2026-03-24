#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # define as product of every left of i
        prefix = [1 for _ in range(len(nums))]
        # define as product of every right of i
        suffix = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        print(prefix)
        print(suffix)
        
        return [prefix[i] * suffix[i] for i in range(len(nums))]


# @lc code=end
