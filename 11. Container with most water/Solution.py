class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0 , len(height) - 1
        maxarea = 0
        while left < right:
            width = right - left
            hei = min(height[right] , height[left])

            area = width * hei

            maxarea = max(maxarea , area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxarea
