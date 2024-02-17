# # class Book:
# #     price =90 #class attribute
# #     def _init_(self, title, num_of_page, cover_color):
# #         self.title = title #instance attribute
# #         self.page_num = num_of_page
# #         self.color = cover_color
# #     name="univel" #class attribute

# #     def buy(self):
# #         print(f"this book {self.title} id sold")
    
# #     def get_tilte(self):
# #         return self.title
    
# #     def change_tilte(self, new_title):
# #         self.title = new_title
# #         print(f"this new title i now {self.title}")
    
# #     def upgrade_price(cls, new_price):
# #         cls.price = new_price
# #         return (f"the new price is now {cls.price}")


# # book1=Book("react beginner", 300,"blue")
# # book2=Book("python for beginner", 400,"yellow" )
# # book3=Book("javascript Mastery", 200,"purple")
# # book1.buy()
# # print(book2.get_tilte())
# # print(book2.change_tilte("django mastery"))
# # print(book1.upgrade_price(22))
# # print(book1.title)
# # print(book2.title)
# # print(book3.title)
# # print(book1.page_num)


# # class Employee:
# #     empCount=0
# #     def _init_(self, name, salary) -> None:
# #          self.name = name
# #          self.salary = salary
# #          Employee.empCount +=1


# # john=Employee("john", 2000)
# # print(john.empCount)

# #class inheritance
# class Animal:
#     def __init__(self, species, leg_count):
#         self.species=species
#         self.leg_count=leg_count

#     def run(self):
#         print("most of the animals can walk")

#     def feed(self):
#         print("animal eat too")

# #single inheritance
# class Bird(Animal):
#     def __init__(self, species, leg_count, feather):
#         super().__init__(species, leg_count)
#         self.feather=feather
#         Animal.__init__(self,type,leg_count)

#         def fly(self):
#             print("brds can fly")

# bird_onj=Bird("aves", 2, "white")
# bird_onj.run()
# bird_onj.feed()
# print(bird_onj.feather)
# #multiple inheritance
# class Mammal:
#     def __init__(self, blood_type):
#         self.blood_type=blood_type

#     def mammal_info(self):
#         print("mammal give birth to their young ones alive")

# class Goat(Animal, Mammal):
#     def __init__(self, species, leg_count, blood_type):
#         super().__init__(species, leg_count)
#         Mammal.__init__(self, blood_type)

# goat1=Goat("he goat", 4, "warm blooded")
# print(goat1.leg_count)
# goat1.mammal_info()
# print(goat1.species)
# print(goat1.blood_type)

# #multi level inheritance
# class Winganimal(Bird):
#     def has_feather(self):
#         print("animal that has feather")

# bat=Winganimal("bat", 2, "brown")
# print(bat.leg_count)
# print(bat.species)
# print(bat.feed())

#CLASSWORK
# class Person:
#     def __init__(self, name, color):
#         self.name=name
#         self.color=color

#     def run(self):
#         print("their can run around by themselves")
#     def feed(self):
#         print("their eat")
# person1=Person("Kehinde", "black")
# print(person1.name)
# print(person1.color)
# person1.feed()

# class Student(Person):
#     def __init__(self, name, color, course, grade):
#         self.course=course
#         self.grade=grade
#         super().__init__(name, color)

#     def __str__(self) -> str:
#         return f"Student: {self.course}"
#     def learn():
#         print("their learn from the teacher")
#     def practice():
#         print("their practice at home")

#     def walk():
#         print("every human can walk")
# student1=Student("Tega", "White", "Backend", 5)
# print(student1.course)
# student1.practice
# student1.learn
# print(student1.name)

        
# class Teacher(Person):
#     def __init__(self, name, color, grade,age):
#         self.grade=grade
#         self.age=age
#         super().__init__(name, color)

#     def walk():
#         print("every teacher can walk as well")

#     def __repr__(self) -> str:
#         return f"Teacher: {self.age} - {self.color}"

# teacher1=Teacher("kehinde", "brown", 4, 30)
# teacher2=Teacher("taiwo", "white", 5, 35)
# print(teacher1.age)
# print(teacher1)
# print(teacher2)
# student1.walk()



class A:
    def __init__(self, a):
        self.a=a 

    def __add__(self, obj):
        # print("yes i have support for the addition you want to carry out")
        return self.a + obj.a
    
    def __sub__(self, obj):
        # return self.a - obj.a
        print("yes i support minus")

    def __multi__(self, obj):
        pass
    
    def __gt__(self, obj):
        return self.a > obj.a
        #     return True
        # else:
        #     return False

obj1=A(4)
obj2=A(6)
ans=obj1 + obj2
print(obj1 - obj2)
print(ans)


class Complex:
    def __init__(self, num1:int, num2:int):
        self.num1=num1
        self.num2=num2
        self.__discount=40

    def __add__(self, obj):
        return self.num1 + obj.num1, self.num2 + obj.num2
    
    def __gt__(self, obj):
        return self.num1 > obj.num1, self.num2 > obj.num2
        #     return True
        # else:
        #     return False
        
    def __lt__(self, obj):
        return self.num1 < obj.num1, self.num2 < obj.num2
        #     return True
        # else:
        #     return False
        
    def get_discount(self):
        return self.__discount


complex_num1=Complex(7, 9)
complex_num2=Complex(9, 12)
ans=complex_num1 + complex_num2
ans=complex_num1 > complex_num2
ans=complex_num1 < complex_num2
print(ans)
print(ans)
print(ans)
print(complex_num1.num1)
print(complex_num1.get_discount())