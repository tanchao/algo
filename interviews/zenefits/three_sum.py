#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        res = []
        if len(nums) < 3:
            return res
        nums.sort()  # sorted array for value judgement
        for i in range(0, len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:  # note skip duplication on every step
                left = i + 1
                right = len(nums) - 1
                while right > left:
                    if nums[i] + nums[left] + nums[right] == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        ''' this is for less than
                        tmp = []
                        tmp.append(nums[i])
                        tmp.append(nums[left])
                        while right > left:
                            tmp.append(right)
                            res.append(tmp)
                            tmp.pop()
                            right -= 1'''
                        right -= 1
                        left += 1
                        while right > left and nums[left] == nums[left - 1]: left += 1
                        while right > left and nums[right] == nums[right + 1]: right -= 1
                    elif nums[i] + nums[left] + nums[right] > 0:
                        while right > left:
                            right -= 1
                            if nums[right] < nums[right + 1]: break
                    else:
                        while right > left:
                            left += 1
                            if nums[left] > nums[left - 1]: break
        return res


if __name__ == '__main__':
    pass