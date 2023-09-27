print("This will tell weather you are eligible for Driving Law and Marriage as per law  or not.")

name= input("What is your name?\nName: ")
age = int(input("What is you age?\nAge: "))
if age < 18:
    print(f"Sorry { name} you are not eligible for Driving License and Marriage.")
elif age <21 and age <18:
    print(f"Sorry { name} you are not eligible for Marriage but you are eligible for Driving License.")
else:
    print(f"Congratulations {name} you are eligible for both Driving License and Marriage.")

