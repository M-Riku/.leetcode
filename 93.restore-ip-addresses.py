#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        ip = []

        def backtracking(start_idx):
            if len(s) > 12:
                return []

            if len(ip) == 4:
                if start_idx == len(s):
                    result.append(".".join(ip))
                return

            if start_idx >= len(s):
                return

            for i in range(start_idx, min(start_idx+3, len(s))):
                sub_ip = s[start_idx:i+1]
                if sub_ip.startswith('0') and len(sub_ip) > 1:
                    continue

                if int(sub_ip) > 255:
                    continue

                ip.append(sub_ip)
                backtracking(i+1)
                ip.pop()

        backtracking(0)
        return result

# @lc code=end
