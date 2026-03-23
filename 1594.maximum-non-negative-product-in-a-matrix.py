#
# @lc app=leetcode id=1594 lang=python3
#
# [1594] Maximum Non Negative Product in a Matrix
#


# @lc code=start
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # let dp[i][j] be the product at grid (i,j)
        # dp[0][0] = grid[0][0]

        max_dp = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        min_dp = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        max_dp[0][0] = grid[0][0]
        min_dp[0][0] = grid[0][0]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    continue
                elif row == 0:
                    max_dp[0][col] = max_dp[0][col - 1] * grid[row][col]
                    min_dp[0][col] = min_dp[0][col - 1] * grid[row][col]
                elif col == 0:
                    max_dp[row][0] = max_dp[row - 1][0] * grid[row][col]
                    min_dp[row][0] = min_dp[row - 1][0] * grid[row][col]
                else:
                    candidates = [
                        max_dp[row - 1][col] * grid[row][col],
                        min_dp[row - 1][col] * grid[row][col],
                        max_dp[row][col - 1] * grid[row][col],
                        min_dp[row][col - 1] * grid[row][col],
                    ]
                    max_dp[row][col] = max(candidates)
                    min_dp[row][col] = min(candidates)
                    
        if max_dp[len(grid)-1][len(grid[0]) - 1] < 0:
            return -1

        return max_dp[len(grid) - 1][len(grid[0]) - 1] % (10**9 + 7)


# @lc code=end
