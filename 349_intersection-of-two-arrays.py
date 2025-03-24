import heapq
from numbers import Number
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result = []
        for i in range(len(nums2)):
            if nums2[i] in set1:
                result.append(nums2[i])
                set1.remove(nums2[i])
        return result

if __name__ == '__main__':
    s = Solution()
    t = [2,7,4,1,8,1]
    c = [2,7,4,1,8,1]
    result = (s.intersection(t, c))
    print(result)