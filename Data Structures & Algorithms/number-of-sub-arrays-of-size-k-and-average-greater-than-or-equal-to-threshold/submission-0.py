class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        window = []
        l = 0
        target = threshold*k

        for r in range(len(arr)):
            window.append(arr[r])

            if r-l+1==k:
                if sum(window) >= target:
                    ans += 1
                window.remove(arr[l])
                l += 1

        return ans
