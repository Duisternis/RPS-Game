from tkinter import *
from tkinter import ttk

from .refresh_leaderboard import refresh
from .game_play import create_window as gameplay_window

def start_app(root, username):

    left = Frame(root)
    right = Frame(root)
    
    left.pack(side=LEFT)
    right.pack(side=RIGHT, fill=BOTH)

    gameplay_window(left, username, right)
    refresh(right, username)
    