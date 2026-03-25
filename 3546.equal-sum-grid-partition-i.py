#
# @lc app=leetcode id=3546 lang=python3
#
# [3546] Equal Sum Grid Partition I
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # the gist of this question is the word "equal", "equal"
        # simply means that when you cut the grid, two halves of the cut
        # are actually "equal" = sum(grid) / 2, divided by two
        # after all is fair and equal right :)
        
        s = 0
        for row in grid:
            s += sum(row);
        
        # we definitely cannot be "equal"
        if s % 2 != 0:
            return False
        
        half = s // 2
        
        # do the row first
        prefix = [0 for _ in range(len(grid))]
        prefix[0] = sum(grid[0])

        if prefix[0] == half:
            return True 

        for row in range(len(grid)):
            prefix[row] = prefix[row - 1] + sum(grid[row])
            if prefix[row] == half:
                return True 
            
        # do the col 
        prefix = [0 for _ in range(len(grid[0]))]
        prefix[0] = sum(r[0] for r in grid) # first column

        if prefix[0] == half:
            return True 

        for col in range(1, len(grid[0])):
            prefix[col] = prefix[col-1] + sum(r[col] for r in grid)
            if prefix[col] == half:
                return True
            
        return False
# @lc code=end

