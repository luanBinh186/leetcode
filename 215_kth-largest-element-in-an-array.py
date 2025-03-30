import heapq
from numbers import Number
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = []
        for n in nums:
            heapq.heappush(l, -n)
        a = 0
        print(l)
        for i in range(k):
            a = heapq.heappop(l)
        return -a

if __name__ == '__main__':
    s = Solution()
    t = [3,2,1,5,6,4]
    k = 2
    result = (s.findKthLargest(t, k))
    print(result)