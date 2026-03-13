price = float(input("please enter price"))
quantity = int(input("please enter quantity"))
member = input("are you member yes or no")

if price >= 100 and quantity >= 3 and member == "yes":
    print("დიდი ფასდაკლება მიიღე")
    print("მადლობა ერთგული მომხმარებლობისთვის")
elif price < 50 and quantity >= 3 and member == "no":
    print("ფასდაკლება მიიღო")
    print("წევრობის შემთხვევაში უფრო მეტს მიიღებ")
elif price < 50 and quantity == 1 and member == "no":
    print("ფასდაკლება არ გეკუთვნის")
    print("მეტი პროდუქტი შეიძინე")
else:
    print("მცირე ფასდაკლება მიიღე")
    print("გმადლობთ შენაძენისთვის")


    
