# Rock Paper Scissors Game in python - @tech-rabi-7

"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""
import random
import tkinter as tk

items = ["rock", "paper", "scissor"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(items)

    result = ""

    if user_choice == computer_choice:
        result = "Tie 🤝"

    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        result = "You Win  ! "
        user_score += 1
    else:
        result = "Computer Wins !"
        computer_score += 1

    result_label.config(
        text=f"You: {user_choice} | Computer: {computer_choice}\n{result}"
    )
    score_label.config(
        text=f"Score → You: {user_score} | Computer: {computer_score}"
    )

# Window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

tk.Label(root, text="Choose One:", font=("Arial", 14)).pack(pady=10)

# Buttons
tk.Button(root, text="Rock", width=10, command=lambda: play("rock")).pack(pady=5)
tk.Button(root, text="Paper", width=10, command=lambda: play("paper")).pack(pady=5)
tk.Button(root, text="Scissor", width=10, command=lambda: play("scissor")).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack()

root.mainloop()