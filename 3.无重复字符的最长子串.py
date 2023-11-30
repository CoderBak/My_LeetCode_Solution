#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        max_len = 0
        for ch in s:
            if ch in lst:
                while ch in lst:
                    lst.pop(0)
            lst.append(ch)
            max_len = max(max_len, len(lst))
        return max_len
# @lc code=end

