class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        c=0
        while l<r:
            c1=min(heights[l],heights[r])*(r-l)
            if(heights[l]>heights[r]):
                r-=1
            elif(heights[l]<heights[r]):
                l+=1
            else:
                l+=1
            c=max(c,c1)
        return c
        