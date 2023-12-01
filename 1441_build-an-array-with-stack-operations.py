class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        num = target.pop(0)
        for i in range(n):
            if num == None:
                return result
            if i + 1 == num:
                result.append("Push")
                num = target.pop(0) if len(target) > 0 else None
            else:
                result.append("Push")
                result.append("Pop")
        return result