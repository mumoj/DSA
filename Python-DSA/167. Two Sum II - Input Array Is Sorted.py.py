class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f, r = 0, len(numbers)-1

        while f<r:
            curr_sum = numbers[f] + numbers[r]
            if curr_sum == target:
                return [f+1, r+1]
            elif curr_sum > target:
                r -= 1
            else:
                f += 1
