# nomer 1
# პითონში ფუნქცია არის კოდის ბლოკი, რომელსაც კონკრეტული დავალების შესრულება შეუძლია

# nomer 2
#1 კოდის ხელახლა გამოყენება – ერთი და იგივე კოდის მრავალჯერ დაწერა არ გვჭირდება.
#2 კოდის ორგანიზება – პროგრამა უფრო მოწესრიგებული და ადვილად წასაკითხი ხდება.
#3 შეცდომების მარტივად გასწორება – პრობლემის პოვნა და გამოსწორება უფრო ადვილია.

# nomer 3
# A parameter is a variable that is declared when a function is defined and allows the function to receive data.

# nomer 4
# Argument არის მნიშვნელობა, რომელსაც ფუნქციის გამოძახების დროს გადავცემთ.

# nomer 5
# პარამეტრი ცვლადია, რომელიც ფუნქციის განსაზღვრისას იწერება.
# არგუმენტი რეალური მნიშვნელობაა, რომელსაც ფუნქციის გამოძახებისას გადავცემთ.

# nomer 6
def repeat_word(word, count):
    for i in range(count):
        print(word)


# nomer 7
def print_numbers(start, end):
    for i in range(start, end):
        print(i)

# nomer 8
def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    print(f"ლუწი რიცხვები: {count}")

# nomer 9
def count_vowels(text):
    vowels = "აიეოუAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    print(f"ხმოვნები: {count}")

# nomer 10
def longest_word(words):
    if not words:
        print("სია ცარიელია")
        return
    longest = max(words, key=len)
    print(f"ყველაზე გრძელი სიტყვა: {longest}")

# nomer 11
def filter_long_words(sentence, n):
    words = sentence.split()
    long_words = [word for word in words if len(word) > n]
    print(long_words)

# nomer 12
names_str = input("შეიყვანეთ სახელები ერთი ხაზით (მაგ: nanuka lasha gio lizi): ")
names = names_str.split()
def name_lengths(names):
    for name in names:
        print(f"{name} - {len(name)}")
name_lengths(names)

# nomer 13
names_str = input("შეიყვანეთ სახელები ერთი ხაზით (მაგ: nika luka ana gio): ")
names = names_str.split()
def name_lengths(names):
    for name in names:
        print(f"{name} - {len(name)}")
name_lengths(names)

# nomer 14
def find_min(numbers):
    if not numbers:
        return None 
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    
    return min_num

# nomer 15
def remove_duplicates(numbers):
    if not numbers:
        print([])
        return []
    unique_list = []
    seen = set()
    
    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique_list.append(num)
    print(unique_list)
    return unique_list

# nomer 16
# ????????











