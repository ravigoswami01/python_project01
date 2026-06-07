# # # print("this is an apple", sep="*",end="-")
# # # print("Ravi")

# # # i = 1
# # # while i <4:
# # #     print(f"hellow world{i}",sep="  ", end="*")
# # #     i += 1

# # # i = 1
# # # while i <=10:
# # #     print(i * 2)
# # #   i += 1
# n = 5
# # # for i in range(1, n+1):
# # #     for j in range(1 , i+1):
# # #         print("*", end="")
# # #     print()


# for i in range(n , 0,-1):
#     for j in range(1 , i +1):
#          print("*", end=" ")
#     print()

# # # for shourtcut formate 
# for i in range(1 , n+1):
#      print("*" * i)

# for i in range(n , 0 , -1):
#      print("* " *  i)
 
# n = 5
# for i in range(1 , n+1):
#     print(" " * (n -i),end="")
#     print("*" * (2 * i -1))

n = 10
for i in range(1,n+1):
    for j in range(1 , i+1):
        print("*",end=" ")
    print()

for i in range(n ,0 ,-1):
    for j in range(1, i+1):
        print("*" , end=" ")
    print("")    