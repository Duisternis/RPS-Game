def reset_elements(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()