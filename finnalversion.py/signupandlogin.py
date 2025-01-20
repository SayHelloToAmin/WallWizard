from rich.console import Console
from rich.panel import Panel
import uuid
import bcrypt
import re
console = Console()
import json
user_file = 'finnalversion.py/Users.json'


# Chcek if username is valid or not
def check_user(username):
    try:
        with open(user_file, 'r') as file:
            users = json.load(file)
            for user in users:
                if user['username'] == username:
                    return user
    except FileNotFoundError:
        return None
#----------------------------------------------


#Check if user already exist in database or not
def user_exists(username=None, email=None):
    try:
        with open(user_file, 'r') as file:
            users = json.load(file)
            for user in users:
                if (user['username'] == username) or (email and user['email'] == email):
                    return True
    except FileNotFoundError:
        return False
    return False
#----------------------------------------------


# Check If Password Is Correct
def check_password(hash_pass, password):
    return bcrypt.checkpw(password.encode('utf-8'), hash_pass.encode('utf-8'))
#----------------------------------------------


#Check if email is in a correct form or not
def check_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None
#----------------------------------------------

#To change the password from normal form to hashed form
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')
#----------------------------------------------


# To save the user in json file
def save_user(user_data):
    try:
        with open(user_file, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    users.append(user_data)

    with open(user_file, 'w') as file:
        json.dump(users, file, indent=4)
#----------------------------------------------


# Sign-Up Function
def sign_up():
    console.print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------" , style="bold yellow")
    console.print(Panel("*Sign up*", style="bold italic yellow"))


    console.print("Enter 'b' to go back to the main.\nIf you want to continue, click on enter: ", style="bold white")
    choice = input()
    if choice.lower() == 'b':
        return
        
    while True:
        while True:
            console.print("Enter Your Username (Enter 'b' to go back to the main): ", style="bold white")
            username = input()
            if not username:
                console.print(Panel("Username Cannot Be Empty !", style="bold red"))
            else:
                break
        if username.lower() == "b":
            return
        if user_exists(username):  # exist => True, not exist => False
            console.print(Panel("Username has already been used!", style="bold red"))
        else:
            break

    while True:
        console.print("Password (at least 8 characters, Enter 'b' to go back to the main menu): ", style="bold white")
        password = input()
        if password.lower() == "b":
            return
        if len(password) < 8:
            console.print(Panel("Password must contain at least 8 characters!", style="bold red"))
        else:
            break

    while True:
        console.print("Email (Enter 'b' to go back to the main): ", style="bold white")
        email = input()
        if email.lower() == "b":
            return
        if not check_email(email):  # valid => True, not valid => False
            console.print(Panel("Email is not valid! Please try again.", style="bold red"))
        elif user_exists(email): 
            console.print(Panel("Email is already been used! Please enter a different email.", style="bold red"))
        else:
            break

    user_id = str(uuid.uuid4())
    hashed_password = hash_password(password)

    user_data = {
        'id': user_id,
        'username': username,
        'password': hashed_password,
        'email': email,
        "games" : 0,
        "wins" : 0
    }

    save_user(user_data)
    console.print(Panel("Sign up was successful!", style="bold green"))
#----------------------------------------------


#Login Function
def login():
    console.print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------" , style="bold yellow")
    console.print(Panel("*Login*", style="bold italic yellow"))
    while True:
        console.print("Enter 'b' to go back to the main.\nIf you want to continue, click on enter: ", style="bold white")
        choice = input()
        if choice.lower() == 'b':
            return
        console.print("Username (Enter 'b' to go back to the main): ", style="bold white")
        username = input()
        if username.lower() == "b":
            return
        user = check_user(username)

        if not user:
            console.print(Panel("Username not found! Please try again.", style="bold red"))
            continue
        else:
            break

    while True:
        console.print("Password (Enter 'b' to go back to the main): ", style="bold white")
        password = input()
        if password.lower() == "b":
            return
        if check_password(user['password'], password):
            console.print(Panel("Login successful!", style="bold green"))
            return user
        else:
            console.print(Panel("Password is incorrect! Please try again.", style="bold red"))
#----------------------------------------------