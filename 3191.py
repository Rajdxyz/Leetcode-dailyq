#we can have a sliding window of len 3 and check at each index if we need to flip that
#index or not.if we need to flip that index we have to flip the whole window
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l=0
        r=2
        res=0
        while r<len(nums):
            if nums[l]==0:
                nums[l]=1
                nums[l+1]^=1
                nums[l+2]^=1
                res+=1
            l+=1
            r+=1
        if nums[l+1]==1 and nums[l]==1:
            return res
        return -1
            