from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high_value = 0
        curr_val = 0
        for i in range(len(gain)):
            curr_val += gain[i]
            if curr_val > high_value:
                high_value = curr_val
        return high_value