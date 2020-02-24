#/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'molength'

'A method of hash map'

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        #生成一个hashmap,以空间换时间。时间复杂度：O(n)
        for k,v in enumerate(nums):
            k_2 = hashmap.get(target-v)
            if k_2 is not None and k!=k_2:
                return [k,k_2]
            hashmap[v] = k
'''            
        for k,v in enumerate(nums):
            hashmap[v] = k
        for k,v in enumerate(nums):
            k_2 = hashmap.get(target-v)
            if k_2 and k!=k_2:
                return [k,k_2]
'''