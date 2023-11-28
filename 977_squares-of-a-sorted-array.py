class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        highest_index = right
        rs = [0 for x in range(len(nums))]
        while left <= right:
            if left == right:
                rs[highest_index] = nums[left] ** 2
                break
            if nums[left] ** 2 > nums[right] ** 2:
                rs[highest_index] = nums[left] ** 2
                left += 1
                highest_index -= 1
            elif nums[left] ** 2 <= nums[right] ** 2:
                rs[highest_index] = nums[right] ** 2
                right -= 1
                highest_index -= 1
        return rs