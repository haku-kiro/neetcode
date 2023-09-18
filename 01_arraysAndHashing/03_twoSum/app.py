# There are two obvious solutions to this problem,
# 1. iterate over the numbers twice trying each combination of numbers, an O(n^2) time, and O(1) space complexity - or,
# 2. iterate over the numbers once - keeping a hashmap of the numbers as you iterate with K:number, V: index for each number
#    subtract the current number from the target to get the required number to sum to the total - if you don't get it, add the
#    number and index to the map and continue. Has an O(n) time and O(n) space complexity

def twoSum(nums, target):
    prev = {}
    for i, v in enumerate(nums):
        diff = target - v
        prevIdx = prev.get(diff, -1)
        if prevIdx == -1:
            prev[v] = i
        else:
            return prevIdx, i
    
    print("no combination found")



if __name__ == "__main__":
    nums = [2, 7, 9, 4, 8]
    target = 13
    print(twoSum(nums, target))
