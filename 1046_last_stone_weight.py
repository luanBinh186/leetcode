import heapq
from numbers import Number
from typing import List

# class DescOrder:
#     def __init__(self, entity):
#         self.entity = entity

#     def __lt__(self, o):
#         return self.entity.__gt__(o.entity)

#     def __repr__(self):
#         return str(self.entity)
    
#     def toNumber(self):
#         return self.entity

# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         hq = []
#         for stone in stones:
#             heapq.heappush(hq, DescOrder(stone))
#         while len(hq) > 1:
#             y = heapq.heappop(hq)
#             x = heapq.heappop(hq)
#             if x != y:
#                 temp = y.toNumber() - x.toNumber()
#                 heapq.heappush(hq, DescOrder(temp))
#         return hq[0].toNumber() if hq else 0

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #heap, O(n)
        stones = [s*(-1) for s in stones]
        heapq.heapify(stones) #works in-palce
        while len(stones) > 1:
            big = -heapq.heappop(stones)
            small = -heapq.heappop(stones)
            if big != small:
                heapq.heappush(stones, small-big)
        return -1*stones[0] if stones else 0

if __name__ == '__main__':
    s = Solution()
    t = [2,7,4,1,8,1]
    result = (s.lastStoneWeight(t))
    print(result)