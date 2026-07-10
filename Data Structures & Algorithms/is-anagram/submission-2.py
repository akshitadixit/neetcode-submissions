class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)) or len(s)!=len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        return s==t