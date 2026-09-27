class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        min1=float("inf")
        while l<r:
            m=(l+r)//2
            if(nums[m]>nums[m+1]):
                return nums[m+1]
            if(nums[m]>nums[r]):
                l=m+1
            elif (nums[m]<=nums[r]):
                r=m
        else:
            return nums[l]