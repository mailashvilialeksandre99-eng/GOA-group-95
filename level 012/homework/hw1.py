# nomer 1
# Sequency - In Python, sequence is the generic term for an ordered set. There are several types of 
# sequences in Python, the following three are the most important
# Selection - the way in which we make a choice between 2 or more possible outcomes in code

# nomer 2
# Indentation - Python indentation is a way of telling a Python interpreter that 
# the group of statements belongs to a particular block of code

# nomer 3

math_point = int(input("Please enter math point"))
english_point = int(input("Please enter english point"))
physics_point = int(input("Please enter physics point"))

if math_point >= 90 and english_point>= 90 and physics_point >= 90:
    print("შესანიშნავი მოსწავლე ხარ")
    print("ყველა საგანში მაღალი შედეგი გაქვს")

elif math_point >= 70 and english_point>= 70 and physics_point >= 70:
    print("კარგი შედეგებია")
    print("სასწავლო წელი წარმატებულია")
elif math_point >= 50 or english_point>= 50 or physics_point >= 50:
    print("ერთ-ერთ საგანში დაბალი ქულა გაქვს")
    print("მეტი სწავლა დაგჭირდება")
else:
    print("შედეგები საშუალოა")
    print("შეგიძლია უკეთესიც")
