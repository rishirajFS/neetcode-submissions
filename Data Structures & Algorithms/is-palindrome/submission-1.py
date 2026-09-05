class Solution:
    def isPalindrome(self, s: str) -> bool:
        news=""
        ss=""
        t=len(s)
        for i in range(t-1,-1,-1):
            if(s[i].isalnum()):
                news+=s[i].lower()
        for j in s:
            if j.isalnum():
                ss+=j.lower()
        print(news,ss)
        if(news==ss):
            return True
        else: 
            return False