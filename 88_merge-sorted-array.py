from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1 # last element in nums1
        j = n - 1 # last element in nums2
        k = m + n - 1 # last element of the merge array in nums1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        return len(nums1)
    
if __name__ == '__main__':
    s = Solution()
    print(s.merge([0], 0, [1], 1))