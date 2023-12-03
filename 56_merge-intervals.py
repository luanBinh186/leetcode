from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals.pop(0)]

        for start, end in intervals:
            if output[-1][1] >= start:
                output[-1][1] = end if end > output[-1][1] else output[-1][1]
            else:
                output.append([start, end])

        return output