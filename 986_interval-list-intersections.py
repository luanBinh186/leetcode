from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        rs = []
        while len(firstList) > 0 and len(secondList) > 0:
            if firstList[0][0] < secondList[0][0]:
                if firstList[0][1] < secondList[0][0]:
                    firstList.pop(0)
                    continue
                elif firstList[0][1] >= secondList[0][0]:
                    rs.append([secondList[0][0], firstList[0][1] if firstList[0][1] <= secondList[0][1] else secondList[0][1]])
                    secondList.pop(0) if firstList[0][1] > secondList[0][1] else firstList.pop(0)
                    continue
            elif secondList[0][0] < firstList[0][0]:
                if secondList[0][1] < firstList[0][0]:
                    secondList.pop(0)
                    continue
                elif secondList[0][1] >= firstList[0][0]:
                    rs.append([firstList[0][0], secondList[0][1] if firstList[0][1] >= secondList[0][1] else firstList[0][1]])
                    secondList.pop(0) if firstList[0][1] > secondList[0][1] else firstList.pop(0)
                    continue
            else:
                if firstList[0][1] > secondList[0][1]:
                    rs.append([secondList[0][0], secondList[0][1]])
                    secondList.pop(0)
                    continue
                else:
                    rs.append([firstList[0][0], firstList[0][1]])
                    firstList.pop(0)
        return rs