# ნომერ 2

score = int(input("please enter score"))
attendance = int(input("please enter attendance"))

if score > 80 and attendance > 90:
    print("შენ შესანიშნავად დაწერე გამოცდა!")

elif score > 50 and attendance > 70:
    print("საშუალოდ დაწერე გამოცდა!")

elif score > 30 and attendance > 50:
    print("გაჭირვებით, მაგრამ ჩააბარე გამოცდა!")