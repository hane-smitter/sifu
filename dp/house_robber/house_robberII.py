'''
House Robber II
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected
and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the
amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.

Exampls
Input: [2,3,2] -> 3
Explanation:
You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
because they are adjacent houses.

Input: [1,2,3,1] -> 4
Explanation:
Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
'''


class Solution:
    '''Time:  O(n) # Space: O(n)'''

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        dont_rob_first_house = self.rob_section(nums[1:])
        dont_rob_last_house = self.rob_section(nums[:-1])

        return max(dont_rob_first_house, dont_rob_last_house)

    def rob_section(self, nums):
        n = len(nums)

        money = [0] * n
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])

        for i in range(2, n):
            rob = nums[i] + money[i-2]
            dont_rob = money[i-1]
            money[i] = max(rob, dont_rob)

        return money[-1]


soln = Solution()
assert soln.rob([1, 2, 3, 1]) == 4
assert soln.rob([2, 3, 2]) == 3
