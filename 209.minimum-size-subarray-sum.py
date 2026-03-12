#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ret = 10000000
        left, right = 0, 0
        s = nums[left]
        
        while right != len(nums) - 1:
            if s < target:
                right += 1 
                s += nums[right]
            
            while s >= target:
                ret = min(ret, right - left + 1)
                s -= nums[left]
                left += 1
        
        if len(nums) == 1 and nums[0] > target: # edge case where input is 7 [8]
            return len(nums)
        
        if ret == 10000000:
            return 0

        return ret

# @lc code=end

