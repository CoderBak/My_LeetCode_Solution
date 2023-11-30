#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxL = 0
        maxS = ""
        for l in range(s.length - 1):
            for r in range(l, s.length):
                sub_str = s[l: r-1]
                rev_str = sub_str[::-1]
                if sub_str == rev_str:
                    if len(sub_str) > maxL:
                        maxS = sub_str
        return maxS
# @lc code=end