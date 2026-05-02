# nomer 1
# append means a built in function that is used to add an item at the end of the list

fruits = ['apple', 'banana', 'grape']
fruits.append("orange")

print (fruits)

# # nomer 2

numbers = []

numbers.append(5)
numbers.append(15)
numbers.append(8)
numbers.append(1000)
numbers.append(7)

print (numbers)

# # nomer 3
words = ['shaurma' , 'khinkali' , 'mwvadi' , 'khatchapuri' , 'katleti']
words.remove('mwvadi')
print(words)

# nomer 4
# pop function removes the last element or the element based on the index given
# remove function the first occurence of the specified element

# nomer 5
movie = ['kungfupanda' , 'fast&furious' , 'Spiderman']
removed = movie.pop()
print ("Removed Element:", removed)
print ("updated list:", movie)

# nomer 6
names = ['alex' , 'zuka' , 'gela' , 'kirishima']
names.insert(0, "Arata")

# nomer 7
numbers1 = [6 , 9 , 5 , 34 , 23 , 56]
numbers1.sort()
print (numbers1)

# nomer 8
# reverse function can make the list go backwards
food = ['hotdog' , 'burger' ,'fried chicken']
food.reverse()
print (food)

# nomer 9
food = ['hotdog' , 'burger' ,'fried chicken']
food.reverse()
print (food)

# nomer 10
brand = ['nike' , 'adidas' , 'puma' ,]
brand.clear()
print (brand)

# nomer 11
sport = ["football" , 'basketball' , 'swimming' , 'jiujitsu']
sport.index()
print (sport)

# nomer 12
word = ['idk' , 'random' , 'word' , 'idea']

word_user = input("Enter a word: ")

if word_user in word:
    index = words.index(word_user)
    print ("Word found at index", index)
else:
    print("not found")

# nomer 13
list = []
for i in range(10):
    num = int (input("Enter a number: "))
    list.append(num)
print("The list is:", numbers)

# nomer 14
koshka = []
for i in range (7):
    num = int(input("Enter a number: "))
    koshka.append(num)
print("Largest number:", koshka)
print("Smallest number", koshka)


















































