class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        p=set(nums)
        c=0
        for i in p:
            if (i-1) not in p:
                c1=0
                while (i+c1) in p:
                    c1+=1
                c=max(c,c1)
        return c

        