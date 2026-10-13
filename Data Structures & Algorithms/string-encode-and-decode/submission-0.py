class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for s in strs:
            result+=str(len(s))+":"+s
        return result

    def decode(self, s: str) -> List[str]:
        # print(s)
        result=[]
        l=0
        r=0
        while r<len(s):
            while s[r]!=":":
                r+=1
            # print(r,s[r])
            next_s_len=int(s[l:r])
            result.append(s[r+1:r+1+next_s_len])
            l=r+1+next_s_len
            r=r+1+next_s_len
        

        return result