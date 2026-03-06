user_name = input("please enter username")
password = input("please enter password")

if user_name == "admin" and password == "superSecretPassword":
    print("მოგესალმები ადმინ!")

if user_name == "guest" and password == "1234":
    print("მომხმარებელი არ მოიძებნა")

else:
    ("მომხმარებელი არ მოიძებნა!")