# numberlist=[2,4,6,8,9,19]
# def find_smallest_number(numberlist):
#    result = min(numberlist)
#    return result

# print(find_smallest_number(numberlist))


# def highest_number(numberlist):
#    highest=numberlist[0]
#    result = max(numberlist)
#    for i in range(len(numberlist)):
#       if numberlist[i] > highest:
#          highest=numberlist[i]
       
#          return result

# print(highest_number(numberlist))


# def cal_sum(*args)->int:
#    print(args)
#    add=sum(args)
#    return add


# print(cal_sum(4,6,7))
# print(cal_sum(3,6,7,9,8))


# def myFun3(**kwargs):
#    print(kwargs)
#    for key, value in kwargs.items():
#       print("%s == %s" % (key, value))


# myFun3(a=3, b=7, course="backend")



#
# def find_index(numbers, target):
#     for index, number in enumerate(numbers):
#         if number == target:
#             return index
        
# numbers = [2, 5, 8, 11]
# target = 8

# index = find_index(numbers, target)

# print(index)




# #no 3 assigment
# def even_num(x):
#    return x
# for n in numbers:
#  b=[2,3,4,5,6,7,8,9,0,10,15]
# d=[]
# def even():
#    # for i in b:
#       if n % 2 == 0:
#          even.append(n)
#          # return d
      
# print(even)
 
#assignment no 1
def find_index(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index

numbers = [2, 5, 8, 11]
target = 2

index = find_index(numbers, target)
print(index)

# #assignment number2 
sam_list = [11, 13, 15, 16, 13, 15, 16, 11] 
print (str(sam_list)) 
result = [] 
for i in sam_list: 
 if i not in result:
  result.append(i) 
print ( str(result))

#assignment number 3
num=[2,3,4,5,6,7,8,9]
def find_even_numbers(num):
    even_numbers = []
    for number in num:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

print(find_even_numbers(num))