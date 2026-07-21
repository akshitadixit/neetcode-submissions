class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sumsofar = 0
        seen = {0:1} # empty prefix subarray at start

        for i in range(len(nums)):
            sumsofar += nums[i]
            if sumsofar-k in seen:
                res += seen[sumsofar-k]
            
            if sumsofar in seen:
                seen[sumsofar] += 1
            else:
                seen[sumsofar] = 1

        return res