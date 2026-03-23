#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""

        have = {}
        need = {}

        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1

        formed = 0
        required = len(need)

        left = 0
        min_len = float("inf")
        result = ""

        for right, c in enumerate(s):
            have[c] = have.get(c, 0) + 1
            if c in need and have[c] == need[c]:
                formed += 1

            while formed == required:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    result = s[left : right + 1]

                left_char = s[left]
                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1
                left += 1
                

        return result


# @lc code=end
