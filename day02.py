num="kehinde"
print(len(num))




a={20, "herny", True, 19, 8}
b={30, 10, 9, 6}
print(len(a))
print(len(b))

class Animal:
    species="bird"
    legcount=20
dove=Animal()

print(hasattr(dove,  "species"))
print(getattr(dove,   "legcount"))
val=getattr(dove,  "parent",  5)
print(val + 5)

a=5
b=3

print('add:', a + b)
print('sub:', a - b)
print('multi:', a * b)
print('division:', a / 5)
print('modu:', a % b)
print('expo:', a ** b)
print('floor:', a // b)

#comparision operators
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)
print(a != b)
print(a == b)

#logical operators
print(a > b and a == b)
print(a < b or a >= b)

#identity operators
print(a is b)
print(a is not b)

a="welcome to class"
print('e' in a)

#sting formatting
sample_str="my name is %s and my age is %d"%('kehinde',  15)
print(sample_str)

prof="backend"
name="kehinde"
sample_str2="my name is {} i am a {} developer".format('kehinde',  "backend")
print(sample_str2)

sample_str3=f"my name is {name} and i am a {prof} developer"
print(sample_str3)

print(sample_str3.capitalize())
print(sample_str2.split())
print(sample_str.title())
print(sample_str2.upper())
print(sample_str3.lower())


