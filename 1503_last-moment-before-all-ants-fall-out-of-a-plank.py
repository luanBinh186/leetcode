from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left.sort()
        mx_left = n if len(left) == 0 else left[len(left) - 1]
        if len(right) == 0:
            return mx_left
        right.sort()
        mx_right = 0 if len(right) == 0 else right[0]
        if len(left) == 0:
            return n - mx_right
        result = n - mx_right if n - mx_right > mx_left else mx_left 
        return result