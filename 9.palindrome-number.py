#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0 :
#             return False
#         S = str(x)
#         start = 0
#         end = len(S) - 1
#         while (True):
#             if (S[start] != S[end]):
#                 return False
#             if (end - start <= 1):
#                 break
#             start += 1
#             end -= 1
#         return True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        nums = []
        start = 10
        while (True):
            i = x % start
            nums.append(i // (start // 10))
            x -= i
            if start > x:
                break
            start *= 10
        
        start = 0
        end = len(nums) - 1
        while(True):
            if nums[start] != nums[end]:
                return False
            if(end - start <= 1):
                break
            start += 1
            end -= 1
        return True

