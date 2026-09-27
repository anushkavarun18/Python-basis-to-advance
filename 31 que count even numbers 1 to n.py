N = int(input("Enter N: "))

count = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        count += 1

print("Count of even numbers:", count)
