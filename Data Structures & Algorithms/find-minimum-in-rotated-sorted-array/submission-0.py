class Solution:
    def binary_search(self, low, high, nums):
        if low == high:
            return nums[low]

        mid = (low + high) // 2

        if nums[mid] > nums[high]:
            return self.binary_search(mid + 1, high, nums)
        else:
            return self.binary_search(low, mid, nums)

    def findMin(self, nums: List[int]) -> int:
        return self.binary_search(0, len(nums) - 1, nums)