# nomer 1
text = "salami samyaro"
clean_text = text.strip()
print(clean_text)

# nomer 2
username = "barley"
clean_username = username.strip()
print(clean_username)

# nomer 3
word = input("enter word: ")
if word.startswith("A"):
    print("the word starts with A")
else:
    print("the word does not start with A")

# nomer 4
website = input("web address: ")
if website.startswith("https"):
    print("the web address is secure")
else:
    print("the web address does not start with 'https'.")

# nomer 5
filename = input("enter filename: ")
if filename.endswith(".py"):
    print("is a python file")
else:
    print("is not a python file")

# nomer 6
email = input("enter email: ")
if email.endswith("@gmail.com"):
    print("is an email address")
else:
    print("is not an email address")

# nomer 7
text = "dog is playing around with cat"
n_text = text.replace("dog", "cat")
print (n_text)

# nomer 8
sentence = input("enter sentence: ")
new_text = sentence.replace(" ", "=")
print(new_text)

# nomer 9
phone_number = input("enter phone number (599-12-34-56): ")
clean_number = phone_number.replace("-", "")
print(clean_number)

# nomer 10
text = input("enter text with extra spaces: ")
clean_text = text.strip()
if clean_text.startswith("Hello"):
    print("text start with 'hello' ")
else:
    print("text does not start with'hello'")

# nomer 11
password = input("enter password: ")
start_capital = password[:1].isupper()
ends_with_1 = password.endswith("1")
if start_capital and ends_with_1:
    print("password valid on both rules")
elif start_capital:
    print("starts with capital letter but does not end with 1.")
elif ends_with_1:
    print("ends with 1 but does not start with capital letter")
else:
    print("does not meet either rule.")

# nomer 12
sentence = input("enter sentence: ")
clean_sentence = sentence.strip()
modded_sentence = clean_sentence.replace(" ", "-")
if modded_sentence.endswith("."):
    print("is valid and ends with a dash.")
else:
    print("does not end with a dash.")

# nomer 13
full_name = input("enter full name (first, last, father's name): ")
part = full_name.split()
for part in part:
    print(part)
print("Total words:", len(part))

# nomer 14
# ???

# nomer 15
numbers = input("enter numbers with seperated spaces: ")
num_list = [int(x) for x in numbers.split()]
total = sum(num_list)
udidesi = max(num_list)
yvelaze_patara = min(num_list)

print("Sum:", total)
print("Largest number:", udidesi)
print("Smallest number:", yvelaze_patara)