#
# @lc app=leetcode id=3693 lang=python3
#
# [3693] Climbing Stairs II
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        if n == 1:
            return costs[0] + 1

        # define dp[i] as the minimum total cost to reach i
        dp = [0 for _ in range(n + 1)]

        dp[0] = 0
        # only one step from 0 -> 1
        dp[1] = costs[0] + 1
        # either one step from 0 -> 2 or two steps 0 -> 1 -> 2
        dp[2] = min(dp[0] + costs[1] + 4, dp[1] + costs[1] + 1)

        # n = 1, 2
        if n < 3:
            return min(costs[1] + (2 - 0) ** 2, dp[1] + costs[1] + (2 - 1) ** 2)

        for i in range(3, n + 1):
            # either j - i = 3
            # or j - i = 2
            # or j - i = 1
            dp[i] = min(
                dp[i - 1] + costs[i - 1] + 1,
                dp[i - 2] + costs[i - 1] + 4,
                dp[i - 3] + costs[i - 1] + 9,
            )

        return dp[n]


# @lc code=end
