#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'molength'

'Binary Search'

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1),len(nums2)
        if m>n:
            nums1,nums2,m,n = nums2,nums1,n,m
        if n==0:
            raise ValueError
        imin,imax,half_len=0,m,(m+n+1)//2
        while imin<=imax:
            i = (imin+imax)//2
            j = half_len - i
            if i<m and nums2[j-1]>nums1[i]:
                #i设置的太小
                imin = i + 1
            elif i>0 and nums1[i-1]>nums2[j]:
                #i设置的太大
                imax = i - 1
            else:
                #i的大小刚好
                if i==0:maxleft = nums2[j-1]
                elif j==0: maxleft = nums1[i-1]
                else: maxleft = max(nums1[i-1],nums2[j-1])
                if(m+n)%2 == 1:
                    return maxleft
                if i==m: minright = nums2[j]
                elif j==n:minright = nums1[i]
                else: minright = min(nums1[i],nums2[j])
                return (maxleft+minright)/2