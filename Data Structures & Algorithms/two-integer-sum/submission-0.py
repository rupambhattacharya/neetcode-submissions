class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}
        for current_index, current_number in enumerate(nums):
            needed_number = target - current_number
            if needed_number in seen_numbers:
                previous_index = seen_numbers[needed_number]
                return [previous_index, current_index]
            seen_numbers[current_number] = current_index

        