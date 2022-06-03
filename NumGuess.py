import random

while True:
    try:
        top_of_range = int(input("Please enter a number : "))
    except Exception as ValueError:
        print("Please enter a +ve numeric value only")
        continue
    except Exception as e:
        print("Something went wrong")
        print(e)
        print(traceback.format_exc())
        break

    if top_of_range <= 0:
        print("Please enter a +ve numeric value only")
        continue
    else:
        #print("You have entered ", top_of_range)
        break

ran_num = random.randint(0,top_of_range)
guessCntr=0
while True:
    print()

    try:
        guessCntr += 1
        inputValue = int(input("Make a guess "))

    except Exception as ValueError:
        print("Please enter a +ve numeric value only")
        continue
    except Exception as e:
        print("Something went wrong")
        print(e)
        print(traceback.format_exc())
        break

    if inputValue == ran_num:
        print("You got it in ", guessCntr, "times.")
        break
    else:
        print("naah ... try again !!")
        continue
