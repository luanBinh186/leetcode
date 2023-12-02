class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if (len(arr) == 2):
            return True
        arr.sort()
        cur_val = abs(arr[0] - arr[1])
        for i in range(1, len(arr) - 1):
            if cur_val == abs(arr[i] - arr[i + 1]):
                continue
            return False
        return True