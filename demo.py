print("hello")
# this is a comment
a=3
print(a)

Str = "Hello World"
print(Str)

b, c, d, = 5, 6.4, "Great"

# Unacceptable Format
# print("Value is "+b)

# Acceptable format
print("{} {}".format("Value is", b))

# To know variable data types
print(type(c)) # change the variable to check the other ones in the console

# create a variable with integer value.
a = 100
print("The type of variable having value", a, " is ", type(a))

# create a variable with float value.
b = 10.2345
print("The type of variable having value", b, " is ", type(b))

# create a variable with complex value.
c = 100+3j
print("The type of variable having value", c, " is ", type(c))
