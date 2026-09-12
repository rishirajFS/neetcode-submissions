class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for ind,num in enumerate(nums):
            if (num) in d.keys():
                return [d[num],ind]
            else: 
                d[target-num]=ind
            
        
        
