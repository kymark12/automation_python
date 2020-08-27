it = 10

while it > 1:
    if it == 9:
        it = it - 1
        continue  # this skips a whole iteration if 9 is reached, it will continue on the rest of the iteration
    if it == 3:
        break  # stops the whole iteration if 3 is reached
    print(it)
    it = it - 1

print('while loop execution is done')
