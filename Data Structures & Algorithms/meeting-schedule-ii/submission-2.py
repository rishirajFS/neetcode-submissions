"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        l1=[]
        l2=[]
        for i in intervals:
            l1.append(i.start)
            l2.append(i.end)
        l1.sort()
        l2.sort()
        st=0
        en=0
        c=0
        res=0
        while st<len(intervals):
            if(l1[st]<l2[en]):
                c+=1
                st+=1
            else: 
                en+=1
                c-=1
            res=max(c,res)
        return res
