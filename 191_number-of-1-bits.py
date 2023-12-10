class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if (n & 1): res += 1
            n //= 2
        return res
