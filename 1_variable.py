hr = "-----------------------------------------------------------"
# multi variable
name1, name2, name3 = "Tanvir", "Sheikh", "Ahmed"

print(name1)
print(name2)
print(name3)

print(hr)

# unpacking a collection
names = ['sheikh', 'tanvir', 'ahmed']
a, b, c = names

print(a)
print(b)
print(c)

print(hr)

# printing multiple variable at once with comma separated
# i) comma separated  -> supports different data types
# ii) using + sign  -> doesn't support different data types
print(a, b, c)
print(name1, name2, name3)
print(a+b+c)

print(hr)


# global keyword
x = "hey dude"
def myFunc():
    global x
    x = "hi dude"

myFunc()

print(x)