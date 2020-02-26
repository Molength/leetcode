#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'molength'

'two pointer'

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        maxarea = 0
        while left<right:
            maxarea = max(maxarea,min(height[left],height[right])*(right-left))
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return maxarea