class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        dup = False
        count_diff = 0
        d_s = {}
        d_g = {}
        for i in range(len(s)):
            if dup == False and i != 0 and (s.count(s[i]) > 1 or goal.count(goal[i]) > 1):
                dup = True
            if s[i] != goal[i]:
                d_s[s[i]] = True
                d_g[goal[i]] = True
                count_diff += 1
            if count_diff > 2:
                return False
        
        diff = set(d_s) - set(d_g)
        if len(diff) != 0:
            return False

        return True if (count_diff == 0 and dup == True) or count_diff == 2 else False