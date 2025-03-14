#first we have to understand the concept of difference array
#using distance array we can update the range in O(1).
#We initiate a n+1 array of zeros.We iterate through each index until the queries dont satisfy the condition of sum+nums[i].
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        pos=0
        i=0
        x=[0]
        curr=0
        for j in nums:
            x.append(0)
        for i in range(len(nums)):
            while curr+x[i]<nums[i]:
                if pos==len(queries):
                    return -1
                l=max(queries[pos][0],i)
                r=queries[pos][1]
                val=queries[pos][2]
                pos+=1
                if r<i:
                    continue
                x[l]+=val
                x[r+1]-=val
            curr+=x[i]
        return pos
