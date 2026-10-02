class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        cl=[]
        res=[]
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        for j in count:
            cl.append([j,count[j]])
        cl.sort(key=lambda x:x[1])
        for t in range(k):
            res.append(cl[-1-t][0])
        return res


