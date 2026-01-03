#WAP to create a quiz

questions = (("What is the name of our galaxy? ")
             ,("Which is the largest planet? ")
             ,("Which is the smallest planey?")
             ,("Which is the fartherst planet"))

options = (("A. Mercury   B. Andromeda   C. Milkyway")
           ,("A. Mercury   B. Earth   C. Jupiter")
           ,("A. Mercury   B. Uranus   C. Jupiter")
           ,("A. Mercury   B. Neptune   C. Saturn"))

answers = []

answer_key = (("C"),("C"),("A"),("B"))

right = 0
wrong = 0


for quiz in range(len(questions)):
    print("-----------------------------------------------------")
    print(questions[quiz])
    print(options[quiz])
    answer = input()
    answers.append(answer)

    if answers[quiz] == answer_key[quiz]:
        print("CORRECT")
        right += 1
    else:
        print("WRONG")
        wrong += 1

print(f"You got {right} CORRECT and {wrong} WRONG")