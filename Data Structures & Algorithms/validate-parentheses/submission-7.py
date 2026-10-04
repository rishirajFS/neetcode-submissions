class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        valid_open={"(":")","{":"}","[":"]"}
        for i in s:
            if stack and i==stack[-1]:
                stack.pop()
            elif i in valid_open:
                stack.append(valid_open[i])
            else:
                return False

            
        if not stack:
            return True
        else:
            return False
            

