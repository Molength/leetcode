class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        #建立一个Hash map
        mapping = {')':'(',']':'[','}':'{'}

        for bra in s:
            #如果是闭括号，那么看栈顶元素是否和它匹配
            if bra in mapping:
                top_element = stack.pop() if stack else '#'
                #如果不匹配，返回False
                if mapping[bra] != top_element:
                    return False
            #如果是开括号，将该元素放入栈顶
            else:
                stack.append(bra)
        #如果栈空了，说明括号对匹配。
        #如果栈不空，匹配不通过。例如:((()
        return not stack