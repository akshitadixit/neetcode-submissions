class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        target = threshold*k
        currsum = sum(arr[:k-1])

        for l in range(len(arr)-k+1):
            currsum += arr[l+k-1]
            if currsum >= target:
                ans += 1
            currsum -= arr[l]

        return ans
