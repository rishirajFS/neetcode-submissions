class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=nums[0]
        maxsum=nums[0]
        for i in nums[1:]:
            cursum=max(i,cursum+i)
            if(cursum>maxsum):
                maxsum=cursum
        return maxsum
