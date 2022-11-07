#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_letter = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = []

        def backtracking(index, cur_word):
            if len(cur_word) == len(digits):
                result.append(cur_word)
                return

            letters = digits_letter[digits[index]]
            for a in letters:
                backtracking(index+1, cur_word+a)

        if digits == "":
            return result
        backtracking(0, '')
        return result
