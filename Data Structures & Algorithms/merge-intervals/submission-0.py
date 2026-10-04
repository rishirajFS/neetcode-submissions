class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        interv=[]
        if not intervals:
            return None
        else:
            intervals.sort(key= lambda x:x[0])
        l,r=intervals[0][0],intervals[0][1]
        for i in intervals[1:]:
            if i[0]<=r:
                r=max(r,i[1])
            else:
                interv.append([l,r])
                l,r=i[0],i[1]
        interv.append([l,r])
        return interv
            
