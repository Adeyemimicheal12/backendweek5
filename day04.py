from functools import reduce


#conditional statement
# if 10 == 11:
#     print("yooh ten is a number")
# else:
#     print("you are not ten")


#     print("running normal codes")

# secret_code=20
# num2=int(input("enter anumber to confirm member"))
# if num2 == secret_code:
#     print("welcome to the club!")
# else:
#     print("your are not a member")


# a="its a cold day"
# b=str(input("enter weathern to confirm"))
# if b == a:
#     print("welcome to the country!")
# else:
#     print("you are not welcome")

# num=20
# num2=30

# if num > num2:
#     print("i am a greater number")
#     a=num - num2
#     print(f"{num} minus {num2} is equal to {a}")
# elif num == num2:
#     print("both number are equal their division is 0")

# elif num % 2 ==0:
#     print(f"{num} is an even number")

# else:
#     print("num is not an actual number")
 
 #looping and iteration
# while loop
# count= 1
# while count <= 6: #true
#     print("hello while loop")
#     print(f"the value of count is {count}")
#     count += 1

# try_limit=4
# try_count=1
# secret_number=6
# guess_number=int(input("guess the secret number : "))
# while guess_number != secret_number:
#     guess_number=int(input("wrong try again : "))
#     try_count += 1
#     if try_count == try_limit:
#         print("oops you are done")
#         break
# print("hurrah you guess it right {guess_number}")

#for loop
# list_name=['herny', 'john', 'peter', 'joy']
# for x in list_name:
#     print(f"mr/mrs {x}")

# for x in range(1, 5):
#     print(f"number of circle is {x}")

even_list=[]
number_list=[9, 2, 6, 4, 8, 13, 19, 7, 3]


# # print(dir(number_list))
# num=iter(number_list)
# print(next(num))
# print(next(num))
# # print(next(num))
# # print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))

# python generator
# def powroftwo(max):
#     n=0
#     while n < max:
#         yield 2 ** n
#         n += 1

# def sample_obj(val):
#     for a in range(val):
#         yield a

# my_iterable_obj=sample_obj(5)
# my_obj=powroftwo(6)
# print(list(my_obj))
# for i in my_iterable_obj:
#     print(i)
def cal_sqt(n):
    return n ** 2


for x in number_list:
 numbers2=[4,6,78,7,9,10]
new_data=map(cal_sqt, numbers2)
print(list(new_data))
if x % 2 == 0:
      even_list.append(x)
print(even_list)

#list comprehension
# even_list2=[x for x in number_list if x % 2 ==0]
# print(even_list2)
#  my_name_list=[x.upper() for x in list_name]
# print(my_name_list)
# sqt_list=[x*x for x in number_list]
# print(sqt_list)

# score_list=[40,50,65,70,73,76,78,81,90]
# def is_a_student(val):
#     return  val >=75

# a_list=list(filter(is_a_student, score_list))
# print(a_list)
# #reduce function

# def add(a, b):
#     return a *  b
# total_val=reduce(add, score_list)
# print(total_val)
