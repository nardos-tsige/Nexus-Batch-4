class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        num = sorted(nums)
        index = []
        for i in range(len(num)):
            if target == num[i]:
                index.append(i)
        return index
