#-----------------------------
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("\n")
        print(key)
        for i in options[question_num-1]:
            print("\n")
            print(i)
        
        guess = int(input("Enter (1, 2, 3, 4): "))
        guesses.append(guess)
        

        correct_guesses += check_answer(questions.get(key), guess)

        question_num += 1

    display_score(correct_guesses, guesses)


#-----------------------------
def check_answer(answer, guess):
    
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
#-----------------------------
    
def display_score(correct_guesses, guesses):
    print("\n")
    print("RESULTS")
    print("\n")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" | ")
    print()

    print("\n")
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" | ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score) + "%")

#-----------------------------
    
def play_again():
    
    response = input("Do you wanna play again? (yes/no)").lower()
    
    if response == "yes":
        return True
    else:
        return False


#-----------------------------

questions = {
    "Which of the following is the biggest planet on our solar system? " : "3",
    "Where was pizza invented? " : "4",
    "Who invented the light bulb?" : "2",
    "How many eyes a spider generally has?" : "1"
}

options = [
            ["1. Naptune", "2. Saturn", "3. Jupiter", "4. The Sun"],
            ["1. Brazil", "2. Russia", "3. Germany", "4. Italy"],
            ["1. Isaac Newton", "2. Thomas Edison", "3. Marie Curie", "4. Rosalind Franklin"],
            ["1. eight", "2. twelve", "3. six", "4. nine"]
]

new_game()

while play_again():
    new_game()

print("Thanks for playing :)")