upper_count = 0
lower_count = 0

text = input("enter word or sentence: ")

for i in range (len(text)):
    if text[i]==text[i].upper():
        upper=upper+1
    else:
        lower=lower+1
print("upper" , "upper" , "lower" , "lower")