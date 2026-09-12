class Solution:

    def encode(self, strs: List[str]) -> str:
        t=""
        for a in strs:
            t+=str(len(a))
            t+="#"
            t+=a
        print(t)
        return t
        
    def decode(self, s: str) -> List[str]:
        l=[]
        i=0
        k=""
        while(i <=len(s)-1):
            
            if s[i]!="#":
                k+=s[i]
            else:
                x=int(k)
                print(k)
                l.append(s[i+1:i+1+x])
                i+=x
                k=""
                if(i>len(s)):
                    break
                
            i+=1
        return l
            

            
