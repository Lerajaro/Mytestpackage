from datetime import date


def try_me():
    
    name = input("type in your name:")
    today = date.today()
    return f"Hello {name}! Today is {today}."
    
    