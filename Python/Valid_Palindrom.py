class Solution(object):
    def isPalindrome(self, s):
        newstring=""
        for i in s:
            if i.isalnum():
                i=i.lower()
                newstring+=i
        rev=newstring[::-1]
        if newstring==rev:
            return True
        else:
            return False
