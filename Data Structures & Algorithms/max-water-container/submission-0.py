class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = -100000
        left = 0
        right = len(heights)-1
        while(left<right):
            if heights[right]>heights[left]:
                maxi = max(maxi,heights[left]*(right-left))
                left +=1
            else:
                maxi = max(maxi,heights[right]*(right-left))
                right-=1
        return maxi
                       