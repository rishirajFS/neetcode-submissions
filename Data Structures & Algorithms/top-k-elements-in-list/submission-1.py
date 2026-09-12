class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(lambda:0)
        freq=[[] for i in range(len(nums)+1)]
        for i in nums:
            count[i]+=1
        for a,b in count.items():
            freq[b].append(a)
        res=[]
        for k1 in range(len(freq)-1,0,-1):
            for l in freq[k1]:
                res.append(l)
                if(len(res)==k):
                    return res
