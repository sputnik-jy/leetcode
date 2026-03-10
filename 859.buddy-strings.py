#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False
        
        d = []
        m = {}
        for i, c in enumerate(goal):
            if s[i] !=  c:
                d.append(i)

            if c in m:
                m[c] += 1
            else:
                m[c] = 1
                   
        if len(d) > 2:
            return False
        
        if s == goal:
            for key, val in m.items():
                if val > 1:
                    return True 
                    
        t= list(s)
        if len(d) == 2:
            t[d[0]], t[d[1]] = t[d[1]], t[d[0]]
        else:
            return False
            
        return "".join(t) == goal

        
# @lc code=end

