from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        output = [intervals.pop(0)]

        for start, end in intervals:
            if output[-1][1] >= start:
                output[-1][1] = end if end > output[-1][1] else output[-1][1]
            else:
                output.append([start, end])

        return output