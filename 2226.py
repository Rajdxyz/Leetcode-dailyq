#the concept is iterate through all possible k's
#edge case:1,array sum is less than k
#To reduce the possibilities of traveling through every k till max(arr), we can apply binary search
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)<k:
            return 0
        r=max(candies)
        l=1
        def check(arr,k,p):
            for i in arr:
                if i<p:
                    continue
                m=i//p
                k-=m
                if k<=0:
                    return True
            return False
        res=0
        while l<=r:
            mid=(l+r)//2
            if check(candies,k,mid):
                l=mid+1
                res=max(res,mid)
            else:
                r=mid-1
        return res

            

        