class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        size = len(heights) - 1
        count = 0
        rightIndex = 0
        leftIndex = size
        while count != size:
            width = leftIndex - rightIndex
            smallerBar = min(heights[rightIndex], heights[leftIndex])
            if width*smallerBar > res:
                res = width*smallerBar
            if(heights[rightIndex] < heights[leftIndex]):
                rightIndex += 1
            else:
                leftIndex-=1
            count += 1
        return res




