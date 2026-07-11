class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l<=r:
            a, b = ord(s[l]), ord(s[r])
            print(a, b)
            if (a<65 or a>90) and (a<97 or a>122) and (a<48 or a>57):
                l += 1
            elif (b<65 or b>90) and (b<97 or b>122) and (b<48 or b>57):
                r -= 1
            # print(s[l], s[r], l, r)
            elif s[l].lower()!=s[r].lower():
                return False
            else:
                l += 1
                r -= 1

        return True