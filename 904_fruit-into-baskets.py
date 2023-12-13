from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        k = 0
        l = 0
        seen = {}
        for i in range(len(fruits)):
            seen[fruits[i]] = seen.get(fruits[i], 0) + 1
            if len(seen) <= 2:
                k = max(k, i - l + 1)
            else:
                seen[fruits[l]] -= 1
                if seen[fruits[l]] == 0:
                    seen.pop(fruits[l])
                l += 1
        return k