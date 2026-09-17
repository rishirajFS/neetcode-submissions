class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        c=0
        for i in range(n+1):
            t=str(bin(i))
            for j in t:
                if(j=="1"):
                    c+=1
            l.append(c)
            c=0
        return l