class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        res = 0
        n = len(height)
        stack = []
        cur =0
        while cur<n:
            while len(stack)!=0 and height[cur] > height[stack[-1]]:
                now = stack.pop()
                if len(stack) == 0:
                    break
                dist = cur - stack[-1] - 1
                bound_height = min(height[cur],height[stack[-1]]) - height[now]
                res = res + dist*bound_height
            stack.append(cur)
            cur = cur + 1
        return res
