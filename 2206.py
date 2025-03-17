class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        x={}
        for i in nums:
            if i in x:
                x[i]+=1
            else:
                x[i]=1
        for v in x.values():
            if v%2!=0:
                return False
        return True