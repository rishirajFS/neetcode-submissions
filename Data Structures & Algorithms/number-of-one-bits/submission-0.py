class Solution:
    def hammingWeight(self, n: int) -> int:
        t=str(bin(n))
        print(t)
        u=0
        for i in t:
            if(i=="1"):
                u+=1
        return u
        
        