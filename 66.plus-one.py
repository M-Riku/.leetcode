#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= -1:
            if i == -1:
                digits = [1] + digits
                break
            else:
                if digits[i] != 9:
                    digits[i] += 1
                    break
                else:
                    digits[i] = 0
                    i -= 1
        return digits

