class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        print(sortedNums)
        results = {}
        for i in range(0, len(sortedNums)):
            rightIndex = i + 1
            leftIndex = len(sortedNums) - 1
            res = None
            while rightIndex < leftIndex:
                res = sortedNums[i] + sortedNums[rightIndex] + sortedNums[leftIndex]
                if res == 0:
                    results[(sortedNums[i], sortedNums[rightIndex], sortedNums[leftIndex])] = 0
                if res < 0:
                    rightIndex += 1
                else:
                    leftIndex -= 1
        print(results.keys())
        return list(results.keys())
