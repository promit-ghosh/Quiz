print("Hello Welcome to the quiz \nHere is your first question\n\n")

print("Question 1 - Which is greater 49 or 94 ?")

try:
    userAns = int(input("Your answer is "))
except ValueError:
    print("Enter numeric input only next time")
    print()
except Exception as e:
    print("Something went wrong")
    print(e)
else:
    if userAns == 94:
        print("yay !! That's correct")
    else:
        print("duh !! That's not correct")

print("Question 2 - Which is a city in India Delhi or Dhaka?")
try:
    userAns = str(input("Your answer is "))
except ValueError:
    print("Enter string input only next time")
    print()
except Exception as e:
    print("Something went wrong")
    print(e)
else:
    if userAns.lower() == "delhi":
        print("yay !! That's correct")
    else:
        print("duh !! That's not correct")
