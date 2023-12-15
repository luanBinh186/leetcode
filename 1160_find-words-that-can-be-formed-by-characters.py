from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = {}
        for i in chars:
            char_count[i] = char_count.get(i, 0) + 1
        total_sum = 0
        for s in words:
            count = 0
            temp_count = char_count.copy()
            for char in s:
                if temp_count.get(char) is None or temp_count[char] <= 0:
                    break
                else:
                    temp_count[char] -= 1
                    count += 1

            if count == len(s):
                total_sum += len(s)

        return total_sum
