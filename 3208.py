#We have to find all groups of k where the colors are alternating
#say we have k=3 we have to find groups of 3 where colors are alternating
#The key is that say we have a window of 7 where the colors are alternating then the number of groups of three are 7-3+1.
#Another problem is that the array is cyclic , we can solve this problem by using modulo(%) where if right pointer exceeds the list then we can place it at index zero using %,eg-len(L)=5,r=7,r%len(L)
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        a=0
        res=0
        curr=1
        n=len(colors)
        while a<len(colors):
            b=a+1
            while b<len(colors)+k-1 and colors[(b-1)%n]!=colors[b%n]:
                b+=1
            if b-a>=k:
                res+=b-a-k+1
            a=b
        return res