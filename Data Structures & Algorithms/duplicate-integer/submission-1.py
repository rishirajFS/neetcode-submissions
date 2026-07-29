class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=[]
        flag=0
        for i in nums:
            if(nums.count(i)>1):
                flag=1
        if(flag==1):
            return True
        else: 
            return False

        