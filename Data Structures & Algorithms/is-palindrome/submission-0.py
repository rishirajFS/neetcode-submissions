class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        q=[]
        for i in s:
            if i.isalnum():
                l.append(i.lower())
                q.append(i.lower())
        l.reverse()
        if(l==q):
            return True
        else:
            return False