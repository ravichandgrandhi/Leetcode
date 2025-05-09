  # Dynamic programming
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        l1 = len(s)
        l2 = len(p)
        ans = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        ans[0][0] = True
        for i in range(2, l2 + 1):
            if p[i - 1] == "*":
                ans[0][i] = ans[0][i - 2]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                # if p[j - 1] == "*":
                #     if p[j - 2] == ".":
                #         ans[i][j] = ans[i][j - 2] or ans[i - 1][j]
                #     else:
                #         if s[i - 1] != p[j - 2]:
                #             ans[i][j] = ans[i][j - 2]
                #         else:
                #             ans[i][j] = ans[i][j - 2] or ans[i - 1][j]
                # elif p[j - 1] == ".":
                #     ans[i][j] = ans[i - 1][j - 1]
                # else:
                #     ans[i][j] = ans[i - 1][j - 1] and s[i - 1] == p[j - 1]
                if p[j - 1] == "*":
                    if p[j - 2] == "." or s[i - 1] == p[j - 2]:
                        ans[i][j] = ans[i][j - 2] or ans[i - 1][j]
                    else:
                        ans[i][j] = ans[i][j - 2]
                elif p[j - 1] == "." or s[i - 1] == p[j - 1]:
                    ans[i][j] = ans[i - 1][j - 1]
        return ans[l1][l2]     