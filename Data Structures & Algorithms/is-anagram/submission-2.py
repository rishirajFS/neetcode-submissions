class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1={}
        l2={}
        for i in s:
            if(i not in l1):
                l1[i]=1
            else:
                l1[i]+=1
        for i in t:
            if(i not in l2):
                l2[i]=1
            else:
                l2[i]+=1
        sorted(l1.items())
        sorted(l2.items())
        if(l1==l2 and len(s)==len(t)):
            return True
        else:
            return False
        