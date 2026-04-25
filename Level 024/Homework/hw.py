# nomer 1
# A mutable object can be modified in place after it’s created.
# An immutable object cannot be changed once it’s created.

# nomer 2
# len can be used with many built-in data types

# nomer 3
word = "გამარჯობა"
print(len(word))

# nomer 4
sentence = input("შეიყვანეთ წინადადება: ")
print(len(sentence))

# nomer 5
# ?

# nomer 6
numbers = [5, 12, 20, 33, 45, 7, 10]

count = 0

for num in numbers:
    if num % 5 == 0:
        count += 1

print("5-ზე გამყოფი რიცხვების რაოდენობა:", count)

# nomer 7
numbers = [14, 28, 35, 56, 20, 84, 7]

for num in numbers:
    if num % 4 == 0 and num % 7 == 0:
        print(num)

# nomer 8
my_list = ["apple", 10, "banana", 25, "cherry", 30]

for i in range(len(my_list)):
    if i % 2 == 0:
        print(my_list[i])

# nomer 9
words = ["apple", "banana", "grape", "watermelon", "kiwi", "strawberry"]

count = 0

for word in words:
    if len(word) > 5:
        count += 1

print("5-ზე მეტი სიგრძის სიტყვების რაოდენობა:", count)

# nomer 10
sentence = "Hello world"

for char in sentence:
    print(char)

# nomer 11
sentence = "Hello world"

for char in sentence:
    if char != " ":
        print(char)

# nomer 12
words = ["apple", "banana", "kiwi", "watermelon"]

for word in words:
    print(word, "-", len(word))