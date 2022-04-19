#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.08 16:04
# @File     : 07-三数之和.py
# @Project  : AGTD


# 给你一个包含 n 个整数的数组 nums，
# 判断 nums 中是否存在三个元素 a，b，c，使得 a + b + c = 0 ？
# 请你找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。


class Solution(object):

    # 双指针法
    def threeSum(self, nums):

        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n):

            left = i + 1
            right = n - 1

            if nums[i] > 0:
                break

            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1

        return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4, 7, -7, 6, -6]

    s = Solution()
    res = s.threeSum(nums)
    print(res)
