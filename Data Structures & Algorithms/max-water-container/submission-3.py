class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        rightIndex = 0
        leftIndex = len(heights) - 1
        while rightIndex < leftIndex:
            width = leftIndex - rightIndex
            smallerBar = min(heights[rightIndex], heights[leftIndex])
            res = max(res, width * smallerBar)
            if heights[rightIndex] < heights[leftIndex]:
                rightIndex += 1
            else:
                leftIndex -= 1
        return res
