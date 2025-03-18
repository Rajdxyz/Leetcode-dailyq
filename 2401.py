#we cannot check every single subarray due to tle.
#concept is when and of two elements is zero then x^y=x+y always.
#Hence instead of a brute force approach we can check a subarray in O(1) using two pointers.
#we can decrement from addsum and from exorsum we can exor the value we want to delete
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        tot=0
        xtot=0
        res=0
        curr=0
        l=0
        for i in range(len(nums)):
            tot+=nums[i]
            xtot^=nums[i]
            curr+=1
            while tot!=xtot: 
                curr-=1
                tot-=nums[l]
                xtot^=nums[l]
                l+=1
            res=max(res,curr)
        return max(curr,res)
