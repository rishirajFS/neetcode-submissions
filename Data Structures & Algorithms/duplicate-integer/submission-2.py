class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag=1
        for i in nums:
            if(nums.count(i)!=1):
                flag=0
                return True
        if flag==1:
            return False