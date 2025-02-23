


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        dic = {}

        for i in range(len(s)):
            # in s string
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
            
            # in t string
            if t[i] in dic:
                dic[t[i]] -= 1
            else:
                dic[t[i]] = -1

        for key in dic:
            if dic[key] != 0:
                return False
        return True
    
if __name__ == '__main__':
    s = Solution()
    result = (s.isAnagram("anagram", "nagaram"))
    print(result)
    