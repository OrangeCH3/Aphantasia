#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.09.29 10:52
# @File     : 02-移除元素.py
# @Project  : AGTD


# 给你一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。


# 双指针法
# 时间复杂度：O(n)
# 空间复杂度：O(1)
def remove_element(nums, val):
    fast = slow = 0

    while fast < len(nums):

        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1

        # 当 fast 指针遇到要删除的元素时停止赋值
        # slow 指针停止移动, fast 指针继续前进
        fast += 1

    return slow, nums


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    res, res1 = remove_element(nums, val)
    print(res, "->", res1)
