class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        p=set(nums)
        l=[]
        for i in range(1,len(nums)+1):
            if i not in p:
                l.append(i)
        return l