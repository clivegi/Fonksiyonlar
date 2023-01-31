# def square(num):
#     return num**2

# number=[1,3,5,6,8,9]
# result=list(map(square,number))
# for item in map(square,number):
#     print(item)
# print(result)

# def square(num):
#     return num**2

# number=[1,3,5,6,8,9]
# result=list(map(lambda num:num**2,number))
# # for item in map(square,number):
# #     print(item)
# print(result)

# square=lambda num:num**2
numbers=[1,3,4,5]
# result=square(3)
# print(result)
check_even= lambda num:num%2==0
# def check_even(num): return num%2==0
# result=list(filter(check_even,numbers))
# result=list(filter(lambda num : num%2==0,numbers))
result=list(filter(check_even,numbers))
print(result)