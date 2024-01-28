class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return (nums[0] - 1) * (nums[1] - 1)
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)