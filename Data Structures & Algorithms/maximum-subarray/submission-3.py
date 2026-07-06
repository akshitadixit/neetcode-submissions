class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algo
        # reset window if currsum is -ve, we discard prev sum

        maxsum = nums[0]
        currsum = 0

        for n in nums:
            currsum = max(currsum, 0)
            currsum += n
            maxsum = max(currsum, maxsum)

        return maxsum




        # maxL, maxR = 0,0
        # l = 0

        # for r in range(len(nums)):
        #     if currsum<0:
        #         currsum = 0
        #         l = r

        #     currsum += nums[r]

        #     if currsum>maxsum:
        #         maxsum = currsum
        #         maxL, maxR = l, r

        # return nums[l:r]