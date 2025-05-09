class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        p1 = len(s) - 1
        while p1 >= 0 and s[p1] == " ":
            p1 -= 1
        p2 = p1
        while p2 >= 0 and s[p2] != " ":
            p2 -= 1
        return p1 - p2