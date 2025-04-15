#Set Mismatch and Smallest Number in Finite Set 

def find_error_nums(nums):
    duplicate = sum(nums) - sum(set(nums))
    missing = sum(range(1, len(nums) + 1)) - sum(set(nums))
    return [duplicate, missing]
def find_smallest_missing(nums):
    smallest = 1
    while smallest in nums:
        smallest += 1
    return smallest
nums = [1, 2, 2, 4]
print("Set Mismatch:", find_error_nums(nums))
print("Smallest Missing Number:", find_smallest_missing(nums))