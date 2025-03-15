#We can come up with a dp solution however it will be O(n*n)
#We can say that capability can be in the range min(nums),max(nums)
#We can simulate the possibilties at that range using binary search
#to check whether a particular capability works we can use greedy approach
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(arr,k,c):
            i=0
            while i<len(arr):
                if arr[i]<=c:
                    k-=1
                    i+=2
                else:
                    i+=1
                if k<=0:
                    return True
            return False
        l=min(nums)
        r=max(nums)
        res=r
        while l<=r:
            mid=(l+r)//2
            if check(nums,k,mid):
                r=mid-1
                res=min(res,mid)
            else:
                l=mid+1
        return res