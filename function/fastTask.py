#  Enumentrate Function using with for loop 


# this  code without enumerate function 

names  = ["adb" , "bca","cdec","bdhdjjh","hdhhd"]
pos = 0

for name in names:
    print(f"this {pos} ------> {name}")
    pos += 1


#  with enumerate function 

for pos , name in enumerate(names):
        print(f"this {pos} ------> {name}")


def find_value( l,target):
    for pos , name in enumerate(l):
        if name == target:
            return pos;
    return -1;


# print(find_value(names , "hdhhd"))

nums = [5,2,8,1,7]


def Find_num(l, target):
    for pos , num in enumerate(l):
        if num == target:
            return pos;
    return - 1

print(Find_num(nums , 9))
