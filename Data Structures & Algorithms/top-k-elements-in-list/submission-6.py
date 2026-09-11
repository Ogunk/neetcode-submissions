class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]

        frequencies = collections.defaultdict(int)
        for num in nums:
            frequencies[num] = frequencies[num] + 1
        
        bucket = [[] for _ in range(len(nums) + 1)] 
        for key, value in frequencies.items():
            bucket[value-1].append(key)
        
        result = []
        for n in range(len(bucket)-1,-1,-1):
            if bucket[n]:
                for num in bucket[n]:
                    result.append(num)
            if len(result) == k:
                break
        return result
