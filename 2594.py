#similar binary search has to be applied where l=1 and r=min(ranks)*cars*cars as to house robber 4
#the part where we check if a time is valid for given cars can be done greedily in O(1) by creating a formula from the equation given in 
#the question i.e n(no. of cars)=(time/rank)**(.5)
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(arr,cars,time):
            ans=0
            for i in arr:
                ans+=int((time/i)**(.5))
                if ans>=cars:
                    return True
            return False
        r=min(ranks)*cars*cars
        l=1
        res=0
        while l<=r:
            mid=(l+r)//2
            if check(ranks,cars,mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res