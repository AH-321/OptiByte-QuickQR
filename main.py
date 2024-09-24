import os
import logo as logo 

python_interpreter = '.venv\\Scripts\\python.exe'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()

    logo.displayLogo()

    print("\n\033[1m" + "OptiByte QuickQR" + "\033[0m")
    print("Please make selection:\n")

    print("1. Run encode.py")
    print("2. Run decode.py")
    print("3. Exit")

    choise = input()

    if choise == "1":
        os.system('cls')
        os.system(f'{python_interpreter} scripts/encode.py')
    elif choise == "2":
        os.system('cls')
        os.system(f'{python_interpreter} scripts/decode.py')
    elif choise == "3":
        exit

main()
