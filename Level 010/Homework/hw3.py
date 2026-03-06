#  ნომერ 3

temperature = int(input("please enter temperature"))
rain = input("1 - raining, 2 - not raining")

if temperature > 25 and rain == "no":
    print("შესანიშნავი ამინდია გასასეირნებლად")

elif temperature > 25 and rain == "yes":
    print("ცხელი და წვიმიანია ჩაფხუტი დაგჭირდება")

elif temperature < 10 or rain == "yes":
    print("სჯობს სახლში დარჩე") 

else:
    print("სასიამოვნო ამინდია!")