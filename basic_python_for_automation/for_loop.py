# for loop

obj = [2, 3, 4, 5, 7, 9]
for i in obj:
    print(i*2)

# sum of First Natural numbers 1+2+3+4+5 = 15
summation = 0
for j in range(1, 6):  # range(i,j) -> i to j-1
    summation = summation + j
print(summation)

print("*********************************")
for k in range(1, 10, 5):
    # third value is the number of skips example: 5 so 1 + 5 = 6 if you add 5 it will be over 10
    # so it won't allow it to go over 10, so 6 is the last output (Check terminal after run)
    print(k)
    print("*****************SKIPPING FIRST INDEX**********************")
for m in range(10):  # 0 - 9 output
    print(m)