print("Hello Welcome to the quiz \nHere is your first question\n\n")


def quiz(typeOfAns, Ques, Ans1, QuesNum):

    rightOrWrong = 'Wrong'
    print("******************")
    print("Question " + QuesNum + " : " + Ques + " ?")

    try:
        if typeOfAns == 'int':
            userAns = int(input("Your answer is - "))
        else:
            if typeOfAns == 'str':
                userAns = str(input("Your answer is -- "))

    except ValueError:
        if typeOfAns == 'int':
            print("Enter numeric input only next time")
        else:
            if typeOfAns == 'str':
                print("Enter string input only next time")
        print()

    except Exception as e:
        print("Something went wrong")
        print(e)
    else:
        if typeOfAns == 'int':
            if str(userAns) == str(Ans1):
                rightOrWrong = 'right'
                
        elif typeOfAns == 'str':
            if str(userAns).lower() == str(Ans1).lower():
                rightOrWrong = 'right'

    if rightOrWrong == 'right':
        print("yay !! That's correct")
    else:
        print("duh !! That's not correct")
    print()
    return(rightOrWrong)

QuesCntr = 1
score=0
rightOrWrong = quiz('int', 'which is greater 49 or 94', '94', str(QuesCntr))
if rightOrWrong == 'right': score +=1

QuesCntr += 1
rightOrWrong = quiz('str', 'Which is a city in India Delhi or Dhaka', 'Delhi', str(QuesCntr))
if rightOrWrong == 'right': score +=1

QuesCntr += 1
rightOrWrong = quiz('int', 'What is the value of 9 x 9', '81', str(QuesCntr))
if rightOrWrong == 'right': score +=1

print("Your score is " + str(score) + " out of " + str(QuesCntr))
