# n1
# In programming, the return statement ends a function and sends a value back to the code that called the function.

# n2
def greet():
    return "Hello, World!"

result = greet()
print(result)

# n3
def square(number):
    return number * number

print(square(2))    # 4
print(square(5))    # 25
print(square(10))   # 100
print(square(-3))   # 9
print(square(0))    # 0

# n4
def add(a, b):
    return a + b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = add(num1, num2)
print("The sum is:", result)

# n5
def add(a, b):
    return a + b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = add(num1, num2)
print("The sum is:", sum_result)

# n6
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

print(count_vowels("Hello"))          
print(count_vowels("Programming"))    
print(count_vowels("AEIOU"))          

# n7
def largest(numbers):
    return max(numbers)

print(largest([3, 7, 2, 9, 5]))       
print(largest([10, 20, 30, 40]))      
print(largest([-5, -2, -8, -1]))      

# n8
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))   
print(sum_list([10, 20, 30]))      
print(sum_list([-1, 1, -2, 2]))    


# n9
def count_letter(text, letter):
    count = 0

    for char in text:
        if char == letter:
            count += 1

    return count

print(count_letter("hello", "l"))        
print(count_letter("programming", "m"))  
print(count_letter("banana", "a"))      

# n10
# ???

# n11
def format_name(name):
    return name.title()

user_name = input("Enter your name: ")

formatted = format_name(user_name)
print("Formatted name:", formatted)









