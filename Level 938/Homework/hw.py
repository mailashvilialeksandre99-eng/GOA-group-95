# nomer 1
# min() → returns the smallest value
# max() → returns the largest value
# sum() → returns the total of all values in an iterable

# nomer 2
# min() helps you find the lowest value
# max() helps you find the highest value
# sum() helps you calculate a total

# nomer 3
def max_difference(numbers):
    return max(numbers) - min(numbers)

print(max_difference([8, 3, 15, 6]))

# nomer 4
def unique_characters(text):
    result = []
    for char in text:
        if text.count(char) == 1:
            result.append(char)
    return result

print(unique_characters("banan"))

# nomer 5
def highest_char(text):
    return max(text)

print(highest_char("Az9"))

# nomer 6
def numbers_summary(numbers):
    return f"Quantity: {len(numbers)} | Sum: {sum(numbers)} | Minimum: {min(numbers)} | Maximum: {max(numbers)}"

print(numbers_summary([5, 10, 15]))

# nomer 7

ord("A")
ord("B")  
ord("C")  


def char_code_sum(text):
    total = 0
    for char in text:
        total += ord(char)
    return total

print(char_code_sum("ABC"))