#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for s in tokens:
            if s in ["+", "-", "*", "/"]:
                num1 = st.pop()
                num2 = st.pop()
                num = int(eval(num2 + s + num1))
                st.append(str(num))
            else:
                st.append(s)
        return int(st[0])
# @lc code=end
