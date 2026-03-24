#
# @lc app=leetcode id=2906 lang=python3
#
# [2906] Construct Product Matrix
#


# @lc code=start
class Solution:
    def flattenIndexToRowCol(self, width, i):
        # row, col
        return i // width , i % width
        
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # this is similar to 238 but I think we can try to flatten this matrix first
        width = len(grid[0])
        height = len(grid)
        n = width * height
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]
        ans = [[1] * width for _ in range(height)] 
        _MOD = 12345
        
        for i in range(1, n):
            row, col = self.flattenIndexToRowCol(width, i - 1)
            prefix[i] = (prefix[i-1] * grid[row][col]) % _MOD
            
        for i in range(n-2, -1, -1):
            row, col = self.flattenIndexToRowCol(width, i + 1)
            suffix[i] = (suffix[i+1] * grid[row][col]) % _MOD
            
        for i in range(n):
            row, col = self.flattenIndexToRowCol(width, i)
            ans[row][col] = (prefix[i] * suffix[i]) % _MOD
            
        return ans


# @lc code=end
