class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        biggest = 0
        fist_point = 0
        for i in range(len(s)):
            if len(s[fist_point:i + 1]) == len(''.join(set(s[fist_point:i + 1]))):
                print(s[fist_point:i + 1])
                biggest = max(biggest, len(s[fist_point:i+1]))
            else:
                fist_point += 1
        return biggest