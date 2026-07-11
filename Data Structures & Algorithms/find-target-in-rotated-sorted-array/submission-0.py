class Solution:
    def binary_search(self, left, right, nums, target):
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                return self.binary_search(left, mid - 1, nums, target)
            else:
                return self.binary_search(mid + 1, right, nums, target)

        else:
            if nums[mid] < target <= nums[right]:
                return self.binary_search(mid + 1, right, nums, target)
            else:
                return self.binary_search(left, mid - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)