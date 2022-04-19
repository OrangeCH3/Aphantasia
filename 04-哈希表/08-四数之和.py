#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.08 16:33
# @File     : 08-四数之和.py
# @Project  : AGTD


# 给定一个包含 n 个整数的数组 nums 和一个目标值 target
# 判断 nums 中是否存在四个元素 a，b，c 和 d
# 使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 注意：答案中不可以包含重复的四元组。


class Solution(object):

    # 双指针法
    def fourSum(self, nums, target):

        res = []
        n = len(nums)
        nums.sort()

        for i in range(n):

            if i > 0 and nums[i] == nums[i - 1]: continue

            for j in range(i + 1, n):

                if j > i + 1 and nums[j] == nums[j - 1]: continue

                p = j + 1
                q = n - 1

                while p < q:
                    if nums[i] + nums[j] + nums[p] + nums[q] > target:
                        q -= 1
                    elif nums[i] + nums[j] + nums[p] + nums[q] < target:
                        p += 1
                    else:
                        res.append([nums[i], nums[j], nums[p], nums[q]])
                        while p < q and nums[p] == nums[p + 1]: p += 1
                        while p < q and nums[q] == nums[q - 1]: q -= 1
                        p += 1
                        q -= 1

        return res


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2, 6, -7, 3, 4, -5]
    target = 2

    s = Solution()
    res = s.fourSum(nums, target)
    print(res)
