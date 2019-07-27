#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def recurAllWords(cur_words, words):
            if words == []:
                all_words.append(cur_words)
            else:
                for word in words:
                    tmp_cur_words = cur_words
                    tmp_cur_words += word
                    tmp_words = words.copy()
                    tmp_words.remove(word)
                    recurAllWords(tmp_cur_words, tmp_words)

        if words == []:
            return []
        all_words = []
        recurAllWords("", words)
        all_words = set(all_words)
        result = []
        for word in all_words:
            i = 0
            while(i < len(s)):
                j = s[i:].find(word)
                if j == -1:
                    break
                else:
                    result.append(i + j)
                    i += j+1
        return result

