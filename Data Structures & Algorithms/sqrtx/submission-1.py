class Solution:
    def mySqrt(self, x: int) -> int:
        if(x==1):
            return 1
        l,r=0,x//2
        res=0
        while(l<=r):
            m=(l+r)//2
            if(m*m>x):
                r=m-1
            if(m*m<x):
                l=m+1
                res=max(m,res)
            if(m*m==x):
                res=m
                break
            
        return res