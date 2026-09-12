class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d1=defaultdict(lambda:1)
        d2=defaultdict(lambda:1)
        for i in range(1,len(nums)):
            d1[i]=nums[i-1]*d1[i-1]
        for j in range(len(nums)-2,-1,-1):
            d2[j]=nums[j+1]*d2[j+1]
        l=[]
        for g in range(len(nums)):
            l.append(d1[g]*d2[g])
        return l
        