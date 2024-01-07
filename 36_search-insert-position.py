class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)
        left, right = 0, len(nums) - 1
        rs = 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
                rs = mid
            else:
                left = mid + 1

        return rs