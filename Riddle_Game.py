# Tricky Riddle game - algorithm
#we need a riddle                                                                 (DONE)
#the user guesses the answer, if it isnt correct, a hint is given                 (DONE)
#if the user cant guess the riddle on the second chance, another hint is given    (DONE)
#if the user still cant guess the correct answer, print "game is over"            (DONE)

guess_count = 1
hint_no = 1
i = 1
limit = 2
ori_answer = "stapler"
hint1 = "It is NOT an Animal.."
hint2 = "It is a very common stationary used by many.."

print("With pointed fangs I sit and wait;")
print("with piercing force I crunch out fate;")
print("grabbing victims, proclaiming might;")
print("physically joining with a single bite. What am I?\n")
answer = input("Write your answer here: ")

while guess_count <= limit:
    if(hint_no == 1):
        if(answer == ori_answer):
            print("Correct Answer! You Win!!")
        else:
            print("Wrong Answer")
            print("Hint Number 1: " + hint1)
            answer = input("Enter the answer: ")
    elif(hint_no == 2):
        if (answer == ori_answer):
            print("Correct Answer! You Win!!")
        else:
            print("Wrong Answer")
            print("Hint Number 2: " + hint2)
            answer = input("Enter the answer: ")

            if(answer == ori_answer):
                print("Correct Answer! You Win!!")
            else:
                print("Sorry, You're out of chances. Game Over.")


    guess_count += 1
    hint_no += 1