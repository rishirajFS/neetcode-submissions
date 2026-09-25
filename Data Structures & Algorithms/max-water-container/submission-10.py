class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0, len(heights)-1
        maxw=0
        while l<r:
            max1=min(heights[l],heights[r])*(r-l)
            if(heights[l]<=heights[r]):
                l+=1
            else:
                r-=1
            maxw=max(max1,maxw)
        return maxw
        