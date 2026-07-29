class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag=1
        if(len(s)!=len(t)):
            flag=0
            return False
        for i in s:
            if(s.count(i)!=t.count(i)):
                flag=0
                return False
        if flag==1:
            return True