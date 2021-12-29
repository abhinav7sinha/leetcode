class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1)

    def binary_search(self, nums, target, start, stop):
        mid = (start+stop)//2
        if start <= stop and mid >= 0:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.binary_search(nums, target, mid+1, stop)
            else:
                return self.binary_search(nums, target, start, mid-1)
        else:
            return -1
