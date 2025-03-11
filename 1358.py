#An easier version of 3306.We hve to find all substrings with all abc.
#We have to arrange a dynamic sliding window.after finding a substring containing abc we can calculate its other substring
#by simply substracting the right pointer with the length of string for all possibilties.then we also have to incremnt the left pointer
#and keep checking at evry increment of left pointer whether substring is valid.
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        check=defaultdict(int)
        l=0
        res=0
        for r in range(len(s)):
            check[s[r]]+=1
            while len(check)==3:
                res+=len(s)-r
                check[s[l]]-=1
                if check[s[l]]==0:
                    check.pop(s[l])
                l+=1
        return res