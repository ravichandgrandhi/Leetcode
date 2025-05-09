
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d={')':'(', '}':'{', ']':'['}
        for c1 in s:
            if c1 in d.keys():
                if not stack or stack.pop() != d[c1]:
                    return False
            else:
                stack.append(c1)
        if stack:
            return False
        return True   