values = [1, 2, "marky", 4, 5]
# List is a data type that allows multiple values and can be different data types

print(values[0])  # follows index
print(values[3])
print(values[-1])  # equals to the last index of the list
# doing ratios (1:3) will actually call indexes in a range for this it's [1] = 2 and then "marky" to 4
print(values[1:3])
values.insert(3, "berbenzana")  # this will insert the string value as a new values on to the 3 index
print(values)  # prints the whole list
values.append("End")  # this will append a new value on the end of the list
print(values)
values[2] = "MARKY"  # invoking the index of the item in the list and replacing/updating its value
del values[0]  # del is a delete command for lists, then specify value[index]
print(values)  # check the updated list
# You'll see on the last line in the output before exit, first index was deleted, third one was updated

# Tuple - Same as LIST data type but immutable/not editable
val = (1, 2, "marky", 4.5)  # tuple is differentiated by parenthesis instead of brackets
print(val[1])
# val[2] = "MARKY"
print(val)
# Dictionary sample
dic = {"a": 2, 4: "mrk", "c": "Hello world"}
print(dic[4])
print(dic["c"])
# building a blank dictionary
blnk_dict = {}
blnk_dict["firstname"] = "Mark Ivan"
blnk_dict["lastname"] = "Berbenzana"
blnk_dict["gender"] = "Male"
print(blnk_dict)
print(blnk_dict["lastname"])
