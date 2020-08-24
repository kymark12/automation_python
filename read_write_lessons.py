# file = open('readwritetest.txt')
#
# # Read all contents of the file
# # print(file.read(5))  # read n number of characters by passing a parameter
#
# # read one single line at a time readline()
# print(file.readline())
# print(file.readline())
#
# # Print line by line using readline method
# # line = file.readline()
# # while line != "":
# #     print(line)
# #     line = file.readline()3
#
# for line in file.readlines():
#     print(line)
# file.close()

# To open a file in 'read-only' add r on the open statement, and w for write ('filename.txt', 'r')
with open('readwritetest.txt', 'r') as reader:
    content = reader.readlines()  # abc, dvdsf, cat, dog, elephant
    reversed(content)  # elephant, dog, cat, dvdsf, abc
    with open('readwritetest.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

