class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        missingValues = []
        for i in range(0, len(nums)):
            missingValue = target - nums[i]
            if nums[i] in missingValues:
                return [missingValues.index(nums[i]), i]
            missingValues.append(missingValue)