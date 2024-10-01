import os
import logo as logo 

if os.name == 'nt':
    python_interpreter = '.venv\\Scripts\\python.exe'
else:
    python_interpreter = '.venv/bin/python'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()

    logo.displayLogo()

    print("\n\033[1m" + "OptiByte QuickQR" + "\033[0m")
    print("Please make selection:\n")

    print("1. New ticket")
    print("2. Scan ticket")
    print("3. Exit")                    
    
    choise = input()

    if choise == "1":
        clear()
        os.system(f'{python_interpreter} scripts/encode.py')
    elif choise == "2":
        clear()
        os.system(f'{python_interpreter} scripts/decode.py')
    elif choise == "3":
        exit

main()
