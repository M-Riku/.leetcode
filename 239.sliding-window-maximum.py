#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque


class MyQueue():
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()

    def push(self, value: int):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        my_queue = MyQueue()
        result = []

        for i in range(k):
            my_queue.push(nums[i])
        result.append(my_queue.front())

        for i in range(k, len(nums)):
            my_queue.pop(nums[i-k])
            my_queue.push(nums[i])
            result.append(my_queue.front())

        return result


# @lc code=end
