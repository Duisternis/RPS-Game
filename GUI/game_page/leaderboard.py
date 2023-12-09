from tkinter import *
import tkinter as tk
from tkinter import ttk

from backend import get_all_content


def create_window(frame, username):

    content = get_all_content.get()
    content = [_ + (_[1]*3 + _[2]*(-2),) for _ in content]
    content = sorted(content, key=lambda x: x[4], reverse=True)

    print(content)

    Label(frame, text='Leaderboard', font=('calibre', 20)).grid(row=0, column=0, sticky='new', pady=10)

    columns = ('Rank', 'User Name', 'Wins', 'Loss', 'Ties', 'Pts')

    tree = ttk.Treeview(frame, columns=columns, show='headings')

    tree.column('Rank', anchor=CENTER, stretch=NO, width=40)
    tree.heading('Rank', text='Rank')
    tree.column('User Name', anchor=CENTER, stretch=NO, width=100)
    tree.heading('User Name', text='User Name')
    tree.column('Wins', anchor=CENTER, stretch=NO, width=40)
    tree.heading('Wins', text='Wins')
    tree.column('Loss', anchor=CENTER, stretch=NO, width=40)
    tree.heading('Loss', text='Loss')
    tree.column('Ties', anchor=CENTER, stretch=NO, width=40)
    tree.heading('Ties', text='Ties')
    tree.column('Pts', anchor=CENTER, stretch=NO, width=40)
    tree.heading('Pts', text='Pts')

    for idx, user in enumerate(content, start=1):
        if user[0] == username:
            current_user_content = (idx,)+user
        tree.insert('', tk.END, values=(idx,)+user)

    tree.grid(row=1, column=0, sticky='nsew')

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')



    user_info_columns = ('Rank', 'User Name', 'Wins', 'Loss', 'Ties', 'Pts')

    user_info_tree = ttk.Treeview(frame, columns=user_info_columns, show='headings', height=0)

    user_info_tree.column('Rank', anchor=CENTER, stretch=NO, width=40)
    user_info_tree.heading('Rank', text=current_user_content[0])
    user_info_tree.column('User Name', anchor=CENTER, stretch=NO, width=100)
    user_info_tree.heading('User Name', text=current_user_content[1])
    user_info_tree.column('Wins', anchor=CENTER, stretch=NO, width=40)
    user_info_tree.heading('Wins', text=current_user_content[2])
    user_info_tree.column('Loss', anchor=CENTER, stretch=NO, width=40)
    user_info_tree.heading('Loss', text=current_user_content[3])
    user_info_tree.column('Ties', anchor=CENTER, stretch=NO, width=40)
    user_info_tree.heading('Ties', text=current_user_content[4])
    user_info_tree.column('Pts', anchor=CENTER, stretch=NO, width=40)
    user_info_tree.heading('Pts', text=current_user_content[5]) 

    user_info_tree.grid(row=2, column=0, sticky='nsew')


    print(current_user_content)