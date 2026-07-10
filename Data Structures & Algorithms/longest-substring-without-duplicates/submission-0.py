class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        if len(set(s))==1:
            return 1

        res, maxLen = 0, 0
        l, r = 0, 0

        while r < len(s) and l<=r:
            if s[r] not in seen:
                res += 1
            else:
                l = max(seen[s[r]] + 1, l)
                res = r-l+1
            
            seen[s[r]] = r
            r += 1
            maxLen = max(maxLen, res)

        return maxLen