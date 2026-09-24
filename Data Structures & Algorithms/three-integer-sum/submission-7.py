class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = {}
        for i in range(0, len(nums)):
            rightIndex = i + 1
            leftIndex = len(nums) - 1
            res = None
            while rightIndex < leftIndex:
                res = nums[i] + nums[rightIndex] + nums[leftIndex]
                if res == 0:
                    results[(nums[i], nums[rightIndex], nums[leftIndex])] = 0
                if res < 0:
                    rightIndex += 1
                else:
                    leftIndex -= 1
        return list(results.keys())
