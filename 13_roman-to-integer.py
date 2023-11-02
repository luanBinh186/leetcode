class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        dic_roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        i = 0
        while i < len(s):
            if i + 1 < len(s) and dic_roman.get(s[i] + s[i + 1]) != None:
                result += dic_roman.get(s[i] + s[i + 1])
                i = i + 2
                continue
            result += dic_roman.get(s[i])
            i = i + 1
        return result