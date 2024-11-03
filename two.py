# 1
twoSum(nums, target):
    hmap = {}
    for i in range(len(nums)):
        hmap[nums[i]] = i
    for i in range(len(nums)):
        if target - nums[i] in hmap and hmap[target - nums[i]] != i:
            return [i, hmap[target - nums[i]]]
