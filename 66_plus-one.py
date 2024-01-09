class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                plus = 1
            else:
                digits[i] += 1
                plus = 0
                break

        if plus == 1:
            return [plus] + digits
        return digits