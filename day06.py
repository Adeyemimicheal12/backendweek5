# nested function parent function calls the inner function
# def outer_function():
#     a=10
#     print("i am the outer function")
#     def secret_fun():
#         print("i am doing a senseitive task")
#     secret_fun()

# outer_function()

# #closure inner function calls the parent function 
# def parent_fuction(a):
#     b=10
#     def inner(y):
#        c= b + a
#        return c * y 
#     return inner

# re=parent_fuction(5)
# print(re(6))

# #decorator
# def add_message(func):
#     def wrapper_func():
#         print("this is my extra message")
#         func()
#     return wrapper_func

# @add_message
# def welcome():
#     print("good bye")

# #decorator for function with argument
# def add_hint(func):
#     def inner_func(a, b):
#         print("this is my extra message")
#         return func(a, b)
#     return inner_func

# @add_hint
# def cal_mul(a, b):
#     res=a * b
#     return res
# # welcome()
# print(cal_mul(2, 4))

#decorator for function avoiding unwanted operationn
# def smart_division(fun):
#     def wrapper_func(a, b): 
#         if a <= 0:
#             print(f"oops the division you want to carry pn cant hold")
#             return
#         return fun(a, b)
#     return wrapper_func
    
# @smart_division
# def cal_div(a, b):
#     res=a / b
#     return res

# print(cal_div(4, 0))

#recursion
# def reducdedby2(num):
#     if num <= 0 :
#         return =








def power(num, topwr):
    if topwr == 0:
        return 1
    else:
        return num * power(num, topwr - 1)

print(power(5, 6))

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    

print(factorial(6))





