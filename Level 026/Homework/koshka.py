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
words = ['shaurma' , 'khinkali' , 'mwvadi' , 'khachapuri' , 'katleti' ,]
words.remove('mwvadi')
print(words)

# nomer 4
# pop function removes the last element or the element based on the index given
# remove function deletes the first occurence of the specified element

# nomer 5
movie = ['kungfupanda' , 'fast&furious' , 'Spiderman']
removed = movie.pop(2)
print ("Removed Element:", removed)
print ("updated list:", movie)

# nomer 6
names = ['alex' , 'zuka' , 'gela' , 'kirishima']
names.insert(2, "Arata")
print (names)
# nomer 7
numbers1 = [6 , 9 , 5 , 34 , 23 , 56]
numbers1.sort()
print (numbers1)

# nomer 8
# reverse function can make the list go backwards
food = ['hotdog' , 'burger' , 'fried chicken']
food.reverse()
print (food)

# nomer 9
food = ['hotdog' , 'burger' ,'fried chicken']
food.reverse()
print (food)

# nomer 10
brand = ['nike' , 'adidas' , 'puma']
brand.clear()
print (brand)

# nomer 11
sport = ["football" , 'basketball' , 'swimming' , 'jiujitsu']
print (sport.index("basketball"))

# nomer 12
word = ['idk' , 'random' , 'word' , 'idea']
word_user = input("Enter a word: ")

if word_user in word:
    index = word.index(word_user)
    print ("Word found at index", index)
else:
    print("not found")

# nomer 13
list = []
for i in range(10):
    num = int(input("Enter a number: "))
    list.append(num)
print("The list is:", list)

# nomer 14
arr = []
for i in range (7):
    num = int(input("Enter a number: "))
    arr.append(num)
arr.sort()
print("Largest number:", arr[6])
print("Smallest number", arr[0])

# 1) ახსენით რას აკეთებს append მეთოდი და მოიყვანეთ მაგალითი
# 2) შექმენით ცარიელი სია. append მეთოდის გამოყენებით დაამატეთ მასში 5 სხვადასხვა რიცხვი და დაპრინტეთ სია
# 3) შექმენით სია სიტყვებით. remove მეთოდის გამოყენებით წაშალეთ ერთ-ერთი სიტყვა და დაპრინტეთ შედეგი
# 4) ახსენით განსხვავება remove და pop მეთოდებს შორის
# 5) შექმენით სია რიცხვებით. pop მეთოდის გამოყენებით ამოიღეთ ბოლო ელემენტი და დაპრინტეთ როგორც ამოღებული ელემენტი, ასევე განახლებული სია
# 6) შექმენით სია. insert მეთოდის გამოყენებით ჩასვით ახალი ელემენტი სიის შუაში
# 7) შექმენით რიცხვების სია. sort მეთოდის გამოყენებით დაალაგეთ ეს სია და დაბეჭდეთ შედეგი
# 8) ახსენით როგორ მუშაობს reverse მეთოდი და მოიყვანეთ მაგალითი
# 9) შექმენით სია სიტყვებით. reverse მეთოდის გამოყენებით შეცვალეთ ელემენტების რიგი
# 10) შექმენით სია და გამოიყენეთ clear მეთოდი. რა შედეგი მიიღეთ?
# 11) შექმენით სია რიცხვებით. გამოიყენეთ index მეთოდი, რომ იპოვოთ კონკრეტული რიცხვის ინდექსი
# 12) შექმენით სია სიტყვებით. მომხმარებელს მოთხოვეთ რაიმე სიტყვა.
#   - თუ ეს სიტყვა არის სიაში იპოვეთ რომელ ინდექსზე დგას ეს სიტყვა
#   - სხვა შემთხვევაში დაპრინტეთ 'ვერ მოიძებნდა'
# 13) შექმენით ცარიელი სია. მომხმარებელს მოთხოვეთ 10 რიცხვი და დაამატეთ ისინი ამ სიაში.
# 14) შექმენით ცარიელი სია. მომხმარებელს მოთხოვეთ 7 რიცხვი და დაამატეთ ისინი ამ სიაში. დაპრინტეთ ამ რიცხვებიდან უდიდესი და უმცირესი რიცხვები
# 15) (|HARD|) შექმენით ცარიელი სია. მომხმარებელს სათითაოდ მოთხოვეთ 10 რიცხვი. სიაში დაამატეთ რიცხვი თუ: 
#   - დადებითია და არის ლუწი
#   - უარყოფითია და არის კენტი
# საბოლოოდ გაიგეთ ამ რიცხვების საშუალო