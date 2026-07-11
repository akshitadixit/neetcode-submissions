from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # maximize the window which contains max occurence of most +k chars
        
        maxf = 0
        l = 0
        cnts = {}
        res = 0

        for r in range(len(s)):
            cnts[s[r]] = cnts.get(s[r], 0) + 1
            maxf = max(maxf, cnts[s[r]])

            # if window is invalid
            if r-l+1 - maxf > k:
                cnts[s[l]] -= 1
                l += 1
            
            else:
                res = max(res, r-l+1)

        return res




