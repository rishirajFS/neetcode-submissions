class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l,r=0,0
        c=0
        se=set()
        while r<len(s):
            if s[r] in se:
                se.remove(s[l])
                l+=1
            else:
                se.add(s[r])
                r+=1
            c=max(c,len(se))
        return c

            
        