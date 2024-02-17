# a=['john', 20, ['sandra', 'joy', 'sarah'],[20,19,22]]

# print(a[2][0])

# first_val=a[2]
# print(first_val[0])

#get the value of 22 from the list
# second_val=a[3]
# print(second_val[2]) 

# del a[1]
# print(a)

# numlist1=[2,5,6,7]
# numlist2=[3,8,9]
# print(numlist1 + numlist2) 
# print([4,6,2] + [9,8,1])
# print(len(numlist1))
# print(5 in numlist1)
# print(numlist2 * 2)

# #fall loops
# for x in numlist1:
    # print(x)

# c=[12,8,7,6,5,4,9]
# print(c)
# c.append(10)
# print(c)
# c.append(13)
# print(c)

# print(c.pop())# remove and return the remove item
# print(c)
# c.insert(6, 40)
# print(c)
# c.sort(reverse=True)
# print(c)
# #when working with number or float list
# highest_num=max(c)
# print(highest_num)
# print()
# lowest_num=min(c)
# print(lowest_num)
# print()
# num=[1,1,1,1,2,3,4,5,6,]
# print(num.count(1))
# print(num.remove(6))


#tuple collection type
# name_tuple=('herny','john','andrew','joy','luckky')
# print(name_tuple[0])#retriving a value with the index
# print(name_tuple[0: 3])#slicing a part of the tuple
# age_tuple=(21,22,19,30,24)
# print(name_tuple + age_tuple)

#set collection
# numb={22, 24, 12, 31, 35}
# num_set={2, 5, 7, 8, 2, 5, 19, 20, 2}
# print(num_set)
# num_set.add(25)
# print(num_set)
# num_set.remove(2)#if the element you are removing does not exist it would give an error
# print(num_set)
# print(num_set.discard(21))#if the element is not present it would not show an error
# print(num_set)
# num_set.update(numb)
# print(num_set)

#union set
people={'herny', 'john', 'james', 'joy'}
student={'james', 'peter', 'joy'}
staff=people.union(student)
print(staff)
new_set=people & student
print(new_set)

# print('herny' in people)

# print(people == student)

#dictionary collection
# student={
#         "name":"joseph",
#         "age": 21,
#         "email":"john419@gmail.com",
#         "address": {
#             "street":"42, mongometry rd",
#             "state":"lagos",
#             "country":"Nigeria",
#             "rules":{
#                 "import_rule":['car' , 'food'],
#                 "supplier":"andrew"
#             }

#         }
#     }
# student["address"]["rules"]["supplier"]="lucky"
# print(student["address"]["rules"]["supplier"])
# student["address"]["rules"]["distributor"]="sandra"
# print(student["address"]["rules"])


# # address=student[address]
# # address.update({'distributor': 'sandra'})
# print(address['country'])

# print(student[1])
# student[1]="peter"
# print(student)
# student["school"]="univelcity"
# print(student)

# print(student["address"]["country"])

# print(student.get('profession'))
# print(student.pop("age"))
# print(student.keys())
# print(student.values())
# print(student)
# student.update({'profession':"backend developer"})
# print(student)
# dup_student=student.copy
# student["school"]="univelcity"
# print(dup_student)
# print(student)



