# This To-Do created by John07-noob
# Sep/10/2020 v1, Sep/24/2020 v2, Okt/9/2020 v3, Okt/15/2020 v4
from colorama import Fore, Back, Style, init
from os import system, name
from time import sleep
init(autoreset=True)

#Colors
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
cyan = Fore.LIGHTCYAN_EX
magenta = Fore.LIGHTMAGENTA_EX

data = "todo" #file name

def clear_screen():
    return system('clear')

def help_page():
    print(f"""{yellow}Welcome To Help Page.
    {yellow}i{cyan} -- insert  {yellow}: {cyan}Insert item to To-Do-App
    {yellow}q{cyan} -- quit    {yellow}: {cyan}Quit from insert command
    {yellow}r{cyan} -- remove  {yellow}: {cyan}Remove item from To-Do-App
    {yellow}l{cyan} -- list    {yellow}: {cyan}List all item in Console
    """)
    while True:
        user = input(f"{cyan}Enter {yellow}({green}q{yellow}) {cyan}to go to the main page: {yellow}")
        if user.lower() == "q":
            clear_screen()
            break
        else:
            clear_screen()
            print(f"{red}Please Enter q")

def list_item():
    try:
        with open(f"{data}.txt", "r") as file:
            print(f"{yellow}Your List of ToDo:")
            print(f"{yellow}=================:")
            print(file.read())
        while True:
            user = input(f"{cyan}Enter {yellow}({green}q{yellow}){cyan} to quit: {yellow}")
            if user.lower() == "q":
                clear_screen()
                break
            else:
                print(f"{red}Please insert q!")
    except FileNotFoundError:
        clear_screen()
        print(f"{red}Must Insert ToDo First!")
        return input(f"{yellow}Press any key to continue....")

def insert_item():
    print(f"{yellow}=====================")
    while True:
        insert_quit = input(f"{cyan}Insert here please{yellow}({green}q{yellow}): ")
        if insert_quit.lower() == "q":
            break
        with open(f"{data}.txt", "a") as file:
            file.writelines(f"{insert_quit}\n")

def remove_item():
    while True:
        try:
            with open(f"{data}.txt", "r") as file:
                print(f"{yellow}Your List (in case you forgot):")
                print(f"{yellow}==============================:")
                print(file.read())
        except FileNotFoundError:
            clear_screen()
            print(f"{red}Must Insert ToDo First!")
            return input(f"{yellow}Press any key to continue....")
        remove = input(f"{cyan}What you want to delete{yellow}({green}q{yellow}): ")
        if remove.lower() == "q":
            break
        else:
            with open(f"{data}.txt", "r") as file:
                lines = file.readlines()
            with open(f"{data}.txt", "w") as file:
                for r in lines:
                    if r.strip("\n") != remove:
                        file.write(r)
            clear_screen()

def shutdown():
    count = 0
    for count in range(2):
        print(f"{red}Shutdown in {count}")
        sleep(1)
        clear_screen()
        count += 1

def menu():
    print(f"{magenta}*{cyan}This is the command{yellow}({green}i{yellow}/{green}r{yellow}/{green}l{yellow}/{green}q{yellow})")

def hmenu():
    print(f"{magenta}*{cyan}Type {green}h{cyan} for more information")


""" Main Code """
print(f"{yellow}WELCOME TO ToDo-APP")
while True:
    menu()
    hmenu()
    ask = input(f"{cyan}Please insert command here: {yellow}")
    if ask == "i":
        clear_screen()
        insert_item()
        clear_screen()
    elif ask == "r":
        clear_screen()
        remove_item()
        clear_screen()
    elif ask == "l":
        clear_screen()
        list_item()
        clear_screen()
    elif ask == "h":
        clear_screen()
        help_page()
    elif ask.lower() == "q":
        clear_screen()
        shutdown()
        exit()
    else:
        print(f"{red}Insert the right command!")
