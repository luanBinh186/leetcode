class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 1
        result = ""
        if len(strs) == 1:
            return strs[0]
        while i > 0:
            temp_str = strs[0][:i]
            if temp_str == "":
                return ""
            for j in range(1, len(strs)):
                if i > len(strs[j]):
                    temp_str = ""
                    i = -1
                    break
                if temp_str != strs[j][:i]:
                    temp_str = ""
                    i = -1
                    break
            result = temp_str if temp_str != "" else result
            i += 1
        return result           