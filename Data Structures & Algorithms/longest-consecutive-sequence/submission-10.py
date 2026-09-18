class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longestSeq = 0
        for num in numSet:
            currentSeq = 0
            if num-1 not in numSet:
                currentSeq += 1
                nextNumber = num + 1
                while nextNumber in numSet:
                    currentSeq += 1
                    nextNumber += 1
                longestSeq = max(longestSeq, currentSeq)
        return longestSeq