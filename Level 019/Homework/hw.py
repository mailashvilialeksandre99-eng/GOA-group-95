# nomer 1
# for loop
for num in range(100, 401):
    if num % 5 == 0 and num % 3 != 0:
        print(num)

# while loop
num = 100
while num <= 400:
    if num % 5 == 0 and num % 3 != 0:
        print(num)
    num += 1

# nomer 2

for num in range(1, 101):
    if num % 2 == 0 and num % 5 == 0:
        print("EvenFive")
    elif num % 2 == 0:
        print("Even")
    elif num % 5 == 0:
        print("Five")
    else:
        print(num)

# nomer 4

n = int(input("enter n: "))

count = 0
for num in range(1, n + 1):
    if num % 3 == 0:
        count += 1

print("Count:", count)

# nomer 5

for num in range (1,51):
    if num % 4 == 0:
        continue
    print(num)

# nomer 6

total = 0

while True:
    num = (input("Enter a number (negative to stop): "))
    
    if num < 0:
        break
    
    total + num

print("Sum:", total)

# nomer 7

