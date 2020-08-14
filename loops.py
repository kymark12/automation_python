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
    print(k)
    print("*****************SKIPPING FIRST INDEX**********************")
for m in range(10):  # 0 - 9 output
    print(m)