class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1=set()
        seen2=set()
        c1=1
        c2=1
        for i in s:
            c1*=ord(i)-64
            if i in seen1:
                continue
            else:
                seen1.add(i)
        for j in t:
            c2*=ord(j)-64
            if j in seen2:
                continue
            else:
                seen2.add(j)
        if seen1==seen2 and c1==c2:
            return True
        else:
            return False