#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    '''
    0 - 0
    1 - 1
    2 - 2
    ...
    9 - 9
    10 - 1
    11 - 2
    12 - 3
    ...
    18 - 9
    19 => 10 - 1
    20 - 2
    21 - 3
    ...
    26 - 8
    27 - 9
    28 => 10 - 1
    30 - 3
    ...
    anything that can wholely divided by 9 => 9
    otherwise return remainder divided by 9
    '''
    def addDigits(self, num: int) -> int:
       if num == 0:
           return 0
       elif num % 9 == 0:
           return 9
       else:
           return num % 9 
# @lc code=end

