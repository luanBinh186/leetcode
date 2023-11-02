class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        m = round(len(num) / 2)
        for i in range(m):
            if num[i] != num[len(num) - 1 - i]:
                return False
        return True     