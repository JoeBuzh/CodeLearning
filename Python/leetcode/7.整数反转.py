#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res_x = int(str(abs(x))[::-1])
        real_x = res_x if x>0 else -1*res_x
        
        if real_x < (-2**31) | real_x > (2**31-1):
            return 0
        else:  
            return real_x
# @lc code=end

