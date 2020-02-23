# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'molength'

'A simplify path method using stack'

class Solution:
    def simplifyPath(self,path:str) -> str:
        stack = []
        for f in path.split('/'):
            '''split方法将path拆分成['','paht1','path2',...'pahtn','']的形式,
            把遇到的仅是pathn的压栈'''
            if f not in ['','.','..']:
                stack.append(f)
            elif f == '..' and stack:
                #遇到..出栈
                stack.pop()
        res = '/'+'/'.join(stack)
        return res