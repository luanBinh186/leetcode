from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        max_sum = current_sum = 0
        n = len(nums)
        seen = {}
        for right in range(len(nums)):
            current_sum += nums[right]
            seen[nums[right]] = seen.get(nums[right], 0) + 1
            if right - left + 1 == k:
                if len(seen) == k:
                    max_sum = max(max_sum, current_sum)
                if seen[nums[left]] > 1:
                    seen[nums[left]] -= 1
                else:
                    seen.pop(nums[left])
                current_sum -= nums[left]
                left += 1
        return max_sum