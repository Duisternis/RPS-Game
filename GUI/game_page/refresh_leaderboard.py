from .leaderboard import create_window as leaderboard_window
from ..reset_frame import reset_elements


def refresh(frame, username):
    reset_elements(frame)
    leaderboard_window(frame, username)