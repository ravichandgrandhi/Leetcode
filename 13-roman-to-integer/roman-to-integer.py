class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        ans = 0
        for i in range(len(s)):
            if i > 0 and d[s[i]] > d[s[i - 1]]:
                ans -= 2 * d[s[i - 1]]
            ans += d[s[i]]
        return ans