
# def find_even_numbers(numbers):
#     even_numbers = []
#     for number in numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)
#     return even_numbersdef find_index(numbers, target):
#     for index, number in enumerate(numbers):
#         if number == target:
#             return index
#     return -1
# numbers = [2, 5, 8, 11]
# target = 8

# index = find_index(numbers, target)
# print(index)
# even_list=[]
# number_list=[9, 2, 6, 4, 8, 13, 19, 7, 3]

# def cal_sqt(n):
#     return n ** 2


# for x in number_list:
#  numbers2=[4,6,78,7,9,10]
# new_data=map(cal_sqt, numbers2)
# print(list(new_data))
# if x % 2 == 0:
#       even_list.append(x)
# print(even_list)

# def find_index(numbers, target):
#     for index, number in enumerate(numbers):
#         if number == target:
#             return index
        
# numbers = [2, 5, 8, 11]
# element = 8
# numbers.index(element)
# index = find_index(numbers, target)

# print(index)

# for i, j in enumerate(['foo', 'bar', 'baz']):
#     if j == 'bar':
#         print(i)

# z = 13
# y = int(input("enter your password to confirm you are a member"))
# if z == y:
#     print("you are welcome to the group")

# elif z != y:
#     print("you are kicked out")



# bet= int(input('enter staking power'))
# if bet >= 10:
#     print(bet * 2 ** 11, "you are allowed to bet")

# elif bet < 10:
#     print("stake should not be less than 10 naira")

# c=[2,3,4,6,9,10]
# c.append(12)
# print(c)

# num1=12
# num2=13
# print(num1 + num2)

# object oriented programming
class Book:
    price=20
    #instance method
    def _init_(self, title, num_of_page, cover_color):
        #instance attribute
        #attributes can be any name of your choice
        #values can be any argument assigned to the constructor _init_ but 
        self.book_title= title
        self.page_num=num_of_page
        self.book_color=cover_color
    name= "Univelcity"


    #instance method
    def buy(self):
        print(f"This book {self.book_title} is sold")

    def get_title(self):
        return self.book_title
    
    def change_title(self, new_title):
        self.book_title= new_title
        print(f"The new book is now {self.book_title}")

    #class method
    @classmethod
    def upgrade_price(cls, new_price):
        cls.book_price= new_price
        print(f"The new book is now {cls.book_price} naira")


book1= Book("React for Beginners", 300, "blue")
book2= Book("Python for Beginners", 500, "green")
book3= Book("Django for Beginners", 400, "red")

print(book2.get_title())
print(book2.change_title("Django mastery"))
book1.buy()
Book.upgrade_price(25)
book1.upgrade_price(500)



# #classwork
# class Animal:
#     def _init_(self, name, color):
#         self.animal_name= name
#         self.animal_color= color
#         # self.animal_sound= sound

#     animal_youngone= "Cub"

#     #instance method
#     def sound(self):
#         print(f"The sound {self.animal_name} makes is Roar")
    
#     def animal(self, new_animal):
#         self.animal_name= new_animal
#         print(f"The animal name is now {self.animal_name}")
    
#     @classmethod
#     def sound(cls, new_sound):
#         cls.animal_sound= new_sound
#         print(f"The sound is now {cls.animal_sound}")

# animal1= Animal("Lion", "Light brown")
# print(animal1.animal_color)
# print(animal1.animal_name)
# print(Animal.animal_youngone)
# Animal.sound("Bleat")
# print(animal1.sound)
        


book1= Book("React for Beginners", 300, "blue")
book2= Book("Python for Beginners", 500, "green")
book3= Book("Django for Beginners", 400, "red")

print(book1.book_color)
print(book2.book_color)
print(book3.book_color)
print(book1.page_num)
print(book2.page_num)
print(book3.page_num)
print(book1.book_title)
print(book2.book_title)
print(book3.book_title)
print(Book.name)


class Employee:
    empcount=0
    def _init_(self,name,salary):
        self.employee_name= name
        self.employee_salary= salary
        Employee.empcount +=1

john= Employee("John", 200000)  
favour= Employee("Favour", 210000) 
sayo= Employee("Sayo",205000)
# print(favour.empcount)
# print(john.empcount)
print(sayo.empcount)
# object oriented programming
class Book:
    price=20
    #instance method
    def _init_(self, title, num_of_page, cover_color):
        #instance attribute
        #attributes can be any name of your choice
        #values can be any argument assigned to the constructor _init_ but 
        self.book_title= title
        self.page_num=num_of_page
        self.book_color=cover_color
    name= "Univelcity"


    #instance method
    def buy(self):
        print(f"This book {self.book_title} is sold")

    def get_title(self):
        return self.book_title
    
    def change_title(self, new_title):
        self.book_title= new_title
        print(f"The new book is now {self.book_title}")

    #class method
    @classmethod
    def upgrade_price(cls, new_price):
        cls.book_price= new_price
        print(f"The new book is now {cls.book_price} naira")


book1= Book("React for Beginners", 300, "blue")
book2= Book("Python for Beginners", 500, "green")
book3= Book("Django for Beginners", 400, "red")

print(book2.get_title())
print(book2.change_title("Django mastery"))
book1.buy()
Book.upgrade_price(25)
# book1.upgrade_price(500)



#classwork
# class Animal:
#     def _init_(self, name, color):
#         self.animal_name= name
#         self.animal_color= color
#         # self.animal_sound= sound

#     animal_youngone= "Cub"

#     #instance method
#     def sound(self):
#         print(f"The sound {self.animal_name} makes is Roar")
    
#     def animal(self, new_animal):
#         self.animal_name= new_animal
#         print(f"The animal name is now {self.animal_name}")
    
#     @classmethod
#     def sound(cls, new_sound):
#         cls.animal_sound= new_sound
#         print(f"The sound is now {cls.animal_sound}")

# animal1= Animal("Lion", "Light brown")
# print(animal1.animal_color)
# print(animal1.animal_name)
# print(Animal.animal_youngone)
# Animal.sound("Bleat")
# print(animal1.sound)
        


book1= Book("React for Beginners", 300, "blue")
book2= Book("Python for Beginners", 500, "green")
book3= Book("Django for Beginners", 400, "red")

print(book1.book_color)
print(book2.book_color)
print(book3.book_color)
print(book1.page_num)
print(book2.page_num)
print(book3.page_num)
print(book1.book_title)
print(book2.book_title)
print(book3.book_title)
print(Book.name)


class Employee:
    empcount=0
    def _init_(self,name,salary):
        self.employee_name= name
        self.employee_salary= salary
        Employee.empcount +=1

john= Employee("John", 200000)  
favour= Employee("Favour", 210000) 
sayo= Employee("Sayo",205000)
print(favour.empcount)
print(john.empcount)
print(sayo.empcount)