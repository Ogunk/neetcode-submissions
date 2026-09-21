class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        leftToRight = ""
        for c in s:
            if c.isalnum():
                leftToRight += c

        rightToLeft = ""
        for c in reversed(s):
            if c.isalnum():
                rightToLeft += c

        print("first is : ", leftToRight)
        print("second is : ", rightToLeft)

        if leftToRight == rightToLeft:
            return True
        else:
            return False