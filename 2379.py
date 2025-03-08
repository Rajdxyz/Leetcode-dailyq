class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        a=0
        b=k-1
        res=k
        m=0
        for i in range(k):
            if blocks[i]=='W':
                m+=1
        res=m
        a+=1
        b+=1
        while b<len(blocks):
            if blocks[a-1]=='W':
                m-=1
            if blocks[b]=='W':
                m+=1
            res=min(m,res)
            b+=1
            a+=1
        return res