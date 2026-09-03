class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        result = False
        for x in nums:
            if x not in seen:
                seen.append(x)
            else:
                result = True
                break
        return result

