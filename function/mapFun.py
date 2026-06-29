nums = [5,2,8,1,7]

def Squered(nums):
    return nums ** 2


value = tuple(map(Squered , nums))

print(value)