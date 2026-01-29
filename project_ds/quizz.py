 #function are made for reusability of code and reduce redundancy
#Flow
#start
#load high score from the file
#ask player name
#show questions one by one
#take answers
#check answers
#increase score
#after quiz end
#compare with high score
#save high score
#end

#questions -> list
#answers
#score ->number
#high_score->file
#player_name -> string

#functions

#load_high_score -> reads old high score
#save_high_score -> saves new high score
#play_quiz -> runs all question
#main -> control program

#code
file_name = "high_score.txt"
score = 0
high_score = 0

#LOAD HIGH SCORE
def load_high_score():
    global high_score
    try:
        #open file in read mode
        file = open(file_name,"r")
        high_score = int(file.read())
        file.close()
    except:
        pass

#SAVE HIGH SCORE
def save_high_score():
    #open file in write mode
    file = open(file_name,"w")
    file.write(str(high_score))
    file.close()

#PLAY QUIZ
def play_quiz():
    global score
    questions = ['What is the output of print(2+3)?','Which data stores true/false?','Which keyword is used to store global variable in the function?']
    answers = ['5', 'Bool','Global']
    for i in range(len(questions)):
        print("\nQ.", questions[i])
        user_answer = input("Your answer: ")
        if user_answer == answers[i]:
            score = score+1
            print("Correct")
        else:
            print("Wrong!!")

#MAIN
def main():
    #global allows updating same high score
    global high_score
    #load previous high score
    load_high_score()
    #ask player name
    name = input("Enter your name: ")
    #start quiz
    play_quiz()
    #print final score
    print("\nQuiz over")
    print(name,"Your score is: ",score)
    #compare score with high_score
    if score>high_score:
        high_score = score
        save_high_score()
    else:
        print("High score is: ",high_score)
main()
    
































