#  ნომერ 4

age = int(input("please enter age"))
student = input("please enter if you are student")

if age < 12 or age > 65:
    print("ბილეთი უფასოა")

if age == "yes" and age > 12:
    print("ბილეთი ნახევარ ფასად")

else:
    print("სრული ფასი უნდა გადაიხადო")