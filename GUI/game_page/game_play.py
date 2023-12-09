from tkinter import *
from PIL import Image, ImageTk
import random

from ..reset_frame import reset_elements
from .refresh_leaderboard import refresh
from backend import insert_request

def battle_result(computer_choice, human_choice):
    if computer_choice == human_choice: return 0

    if human_choice == 0:
        if computer_choice == 1: return -1
        else: return 1
    elif human_choice == 1:
        if computer_choice == 2: return -1
        else: return 1
    else:
        if computer_choice == 0: return -1
        else: return 1


def gameplay_handler(frame, choice, icons, username, leaderboard_frame):
    reset_elements(frame)

    random_choice = random.choice([0, 1, 2])

    human_image = icons[choice].resize((100, 100), Image.Resampling.LANCZOS)
    human_image = ImageTk.PhotoImage(human_image)

    computer_image = icons[random_choice].resize((100, 100), Image.Resampling.LANCZOS)
    computer_image = ImageTk.PhotoImage(computer_image)

    label_human = Label(frame, image=human_image)
    label_human.image = human_image
    label_human.grid(row=0, column=0)

    result = battle_result(random_choice, choice)

    insert_request.post(username, result)

    if (result == 1): result = "Win"
    if (result == 0): result = "Draw"
    if (result == -1): result = "Loss"

    Label(frame, text=result).grid(row=0, column=1)

    label_computer = Label(frame, image=computer_image)
    label_computer.image = computer_image
    label_computer.grid(row=0, column=2)

    refresh(leaderboard_frame, username)


def create_window(frame, username, leaderboard_frame):

    gameplay_frame = Frame(frame)
    gameplay_frame.grid(row=0, column=0, columnspan=4, pady=(0, 50), padx=30)

    rock_icon = Image.open("./GUI/assets/rock.png")
    resized_rock_icon = rock_icon.resize((35, 35), Image.Resampling.LANCZOS)
    resized_rock_icon = ImageTk.PhotoImage(resized_rock_icon)

    paper_icon = Image.open("./GUI/assets/paper.png")
    resized_paper_icon = paper_icon.resize((35, 35), Image.Resampling.LANCZOS)
    resized_paper_icon = ImageTk.PhotoImage(resized_paper_icon)

    scissors_icon = Image.open("./GUI/assets/scissors.png")
    resized_scissors_icon = scissors_icon.resize((35, 35), Image.Resampling.LANCZOS)
    resized_scissors_icon = ImageTk.PhotoImage(resized_scissors_icon)

    icons = [rock_icon, paper_icon, scissors_icon]

    rock_button = Button(frame, text = '', image = resized_rock_icon, width=35, height=35, command=lambda: gameplay_handler(gameplay_frame, 0, icons, username, leaderboard_frame))
    rock_button.image = resized_rock_icon
    rock_button.grid(row=1, column=0, padx=(41, 0)) 

    paper_button = Button(frame, text = '', image = resized_paper_icon, width=35, height=35, command=lambda: gameplay_handler(gameplay_frame, 1, icons, username, leaderboard_frame))
    paper_button.image = resized_paper_icon
    paper_button.grid(row=1, column=1) 

    scissors_button = Button(frame, text = '', image = resized_scissors_icon, width=35, height=35, command=lambda: gameplay_handler(gameplay_frame, 2, icons, username, leaderboard_frame))
    scissors_button.image = resized_scissors_icon
    scissors_button.grid(row=1, column=2) 



    display_rock_icon = rock_icon.resize((100, 100), Image.Resampling.LANCZOS)
    display_rock_icon = ImageTk.PhotoImage(display_rock_icon)

    label_human = Label(gameplay_frame, image=display_rock_icon)
    label_human.image = display_rock_icon
    label_human.grid(row=0, column=0)

    Label(gameplay_frame, text="Choose").grid(row=0, column=1)

    label_computer = Label(gameplay_frame, image=display_rock_icon)
    label_computer.image = display_rock_icon
    label_computer.grid(row=0, column=2)
  