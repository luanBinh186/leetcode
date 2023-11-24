class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        l = len(nums)
        if l == 0:
            return result
        if l == 1:
            return [str(nums[0])]
        start = nums[0]
        end = nums[0]

        def insertText(start: int, end: int, result: List[str]):
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(end))

        for i in range(1, len(nums)):
            if nums[i] - end > 1:
                insertText(start, end, result)
                start = nums[i]
                end = nums[i]
            else:
                end = nums[i]

            if i == len(nums) - 1:
                insertText(start, end, result)
        return result       