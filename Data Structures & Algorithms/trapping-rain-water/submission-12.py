class Solution:
    def trap(self, height: List[int]) -> int:
        size=len(height)
        maxLeft = [0] * size
        maxRight = [0] * size
        currentMax = height[0]

        for i in range(0, size):
            maxLeft[i] = currentMax
            if height[i] > currentMax:
                currentMax = height[i]

        currentMax = height[size-1]
        for i in range(size-1, 0, -1):
            maxRight[i] = currentMax
            if height[i] > currentMax:
                currentMax = height[i]
        
        trappedWater = 0
        for i in range(0, size):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            if water > 0:
                trappedWater+= water
        
        return trappedWater