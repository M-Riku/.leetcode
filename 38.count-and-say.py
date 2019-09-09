#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
class Solution:
    def countAndSay(self, n: int) -> str:
        def cur(cas, i):
            if i == n:
                return cas
            else:
                new_cas = ""
                c = 1
                for s in range(len(cas)):
                    if s == len(cas) - 1:
                        new_cas += (str(c) + cas[s])
                        break
                    if cas[s] == cas[s+1]:
                        c += 1
                    else:
                        new_cas += (str(c) + cas[s])
                        c = 1
                return cur(new_cas, i+1)
        return cur("1", 1)

