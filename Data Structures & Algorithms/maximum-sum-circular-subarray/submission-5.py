class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currsum = nums[0]
        maxsum = nums[0]
        minsum = nums[0]

        for r in range(1,len(nums)):
            currsum = max(currsum, 0)
            currsum += nums[r]
            maxsum = max(currsum, maxsum)

        currsum = nums[0]

        for r in range(1,len(nums)):
            currsum = min(currsum, 0)
            currsum += nums[r]
            minsum = min(currsum, minsum)

        print(minsum, maxsum)

        if maxsum > sum(nums)-minsum:
            return maxsum
        elif sum(nums)-minsum==0:
            return maxsum
        return sum(nums)-minsum
            