class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        signs = []

        for x in range(len(arr)-1):
            if arr[x] < arr[x+1]:
                signs.append(1)
            elif arr[x] > arr[x+1]:
                signs.append(-1)
            else:
                signs.append(0)

        # now we have signs, we want to find longest subarray with alternating signs

        l, r = 0, 0
        maxwin = 1
        while r < len(signs):
            if r>0 and signs[r] + signs[r-1] == 0 and signs[r]!=0:
                pass
            elif signs[r]==0:
                l = r+1
            else:
                l =r

            r += 1
            maxwin = max(maxwin, r-l+1)

        return maxwin
