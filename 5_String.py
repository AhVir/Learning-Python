hr = "-------------------------------"

# multiline string
str = '''hi tanvir, 
I know you're having a very very
tough situation, but trust me, 
this too shall pass'''

print(str)

print(hr)

str2 = """Again Tanvir,
be strong & be brave. It's just a
ups & downs of life"""

print(str2)

print(hr)

# an element of a string array is still a string, there's nothing
# called char in python

x1 = str[0]
print(x1 , ", and data type: " , type(x1))

print(hr)

# looping through a string
for x in str:
    print(x, end="")
print() # for line break

print(hr)

# string length

print("length of str is ", len(str))


print(hr)

# check certain phrase or character in a string

print("tanvir" in str)
print("tanvir" not in str)

if "tanvir" in str:
    print("yes, my name is there in the string")
else:
    print("no, my name is not there")
