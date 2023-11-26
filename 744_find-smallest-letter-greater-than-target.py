class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        output_char = letters[0]

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                output_char = letters[mid]
                right = mid - 1
            else:
                left = mid + 1

        return output_char