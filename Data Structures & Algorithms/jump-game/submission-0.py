class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curpos=0
        goal=len(nums)-1
        flag=0
        for i in range(len(nums)):
            if i>curpos:
                return False
            jumpto=max(i,i+nums[i])
            curpos=max(jumpto,curpos)
            if(curpos>=goal):
                flag=1
                return True
        if(flag==0):
            return False