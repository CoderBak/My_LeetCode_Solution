#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_lst = [target - num for num in nums]
        original_num = set(nums)
        set_x = original_num.intersection(set(new_lst))
        for x in set_x:
            a = new_lst.index(x)
            b = nums.index(x)
            if a == b:
                new_lst.remove(x)
                return [new_lst.index(x) + 1, b]
            else:
                return [a, b]
# @lc code=end

