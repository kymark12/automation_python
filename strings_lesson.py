strng = "MarkIvanBerbenzana"
str1 = '@zenrooms.com'
str3 = "MarkIvan"

print(strng[5])  # this will output 'v' based on the index position of 'v' = 5

print(strng[0:4])  # this will out characters from index 0 - 4 which is "Mark"

print(strng+str1)  # concatenating strings

print(str3 in strng)  # checks substring value on another string

var = str1.split('.')  # splits strings on a designated character/letter ('.')
print(var)
print(var[0])

str4 = " Ivan "
print(str4.strip())  # removes all white spaces
print(str4.lstrip())  # removes left white spaces
print(str4.rstrip())  # removes right white spaces
