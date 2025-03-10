#we have to solve it in O(n).
#to do that the first part is to understand the fact that:(substrings with at least k consonants)-(substrings with at least k-1 consonants)
#that formula will thus equate to substrings with exactly k consonants.
#thus to find substrings to find atleast k and k+1 substrings we have to arrange a dynamic sliding window to find them.
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleastk(k):
            res=0
            l=0
            n=len(word)
            vow=defaultdict(int)
            non_vow=0
            for r in range(n):
                if word[r] in "aeiou":
                    vow[word[r]]+=1
                else:
                    non_vow+=1
                while len(vow)==5 and non_vow>=k:
                    res+=n-r
                    if word[l] in "aeiou":
                        vow[word[l]]-=1
                    else:
                        non_vow-=1
                    if vow[word[l]]==0:
                        vow.pop(word[l])
                    l+=1
            return res
        return atleastk(k)-atleastk(k+1)