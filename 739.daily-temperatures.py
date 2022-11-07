#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        st = []

        for i in range(len(temperatures)):
            cur_temp = temperatures[i]
            while st and cur_temp > st[-1][1]:
                temp = st.pop()
                result[temp[0]] = i - temp[0]
            st.append([i, cur_temp])

        return result

# @lc code=end
