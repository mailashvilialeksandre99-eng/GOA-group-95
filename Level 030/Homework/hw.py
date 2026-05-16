# nomer 1
text = "Hello World"
result = text.lower()

print(result)
# Python-ში lower() მეთოდი სტრიქონის (string) ყველა დიდ ასოს პატარა ასოდ გარდაქმნის.

# nomer 2
text = "gaumarjos bratan"

small_text = text.lower()

print(small_text)

# nomer 3
# Python-ში upper() მეთოდი სტრიქონის (string) ყველა პატარა ასოს დიდ ასოდ გარდაქმნის.
text = "nugzara"
result = text.upper()

print(result)

# nomer 4
word = input("enter word: ")

massive_word = word.upper()

print(massive_word)

# nomer 5
# Python-ში title() მეთოდი სტრიქონის თითოეული სიტყვის პირველ ასოს დიდად აქცევს ხოლო დანარჩენ ასოებს პატარად
text = "gaumarjos world"

result = text.title()

print(result)

# nomer 6
words = ["shaurma", "xinkali", "mwvadi"]

for word in words:
    print(word.title())

# nomer 7
text = "sHaUrMa"

result = text.swapcase()

print(result)

# nomer 8
text = "mwvadi"

count_a = text.count("a")

print(count_a)

# nomer 9
sentence = input("enter sentence: ")
symbol = input("enter symbol: ")

count_symbol = sentence.count(symbol)

print("meet symbol", count_symbol, "yet")

# nomer 10
name = input("enter name: ")
surname = input("enter last_name: ")

print(name.title())
print(surname.title())

# nomer 11
sentence = input("enter sentence: ")

vowels = "aeiou"

count = 0

for letter in sentence:
    if letter in vowels:
        count += 1

print("sentence:", count)

# nomer 12
# ver gavige :D