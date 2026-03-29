#
# @lc app=leetcode id=2839 lang=python3
#
# [2839] Check if Strings Can be Made Equal With Operations I
#


# @lc code=start
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return True

        s1 = list(s1)
        s2 = list(s2)

        s2[0], s2[2] = s2[2], s2[0]

        if s1 != s2:
            s2[1], s2[3] = s2[3], s2[1]

        if s1 != s2:
            s2[0], s2[2] = s2[2], s2[0]

        return s1 == s2


# @lc code=end
