import os
import sys
from typing import NoReturn
from logo import displayLogo
from scripts.decode import decodeQRCode
from scripts.encode import generateNewQRCode

# TODO: Check for errors when decoding QR codes (i dont have a webcam but it should work)
# Hope these changes are welcomed, @AH-321! :D

def clearScreen() -> None:
    """Clear the console screen in a cross-platform way."""
    os.system('cls' if os.name == 'nt' else 'clear')


def getPythonInterpreter() -> str:
    """Get the appropriate Python interpreter command for the current OS."""
    return 'python' if os.name == 'nt' else 'python3'


def displayMenu() -> None:
    """Display the main menu options."""
    print("\n\033[1mOptiByte QuickQR\033[0m")
    print("Please make selection:\n")
    print("1. New ticket")
    print("2. Scan ticket")
    print("3. Exit")


def handleUserChoice(choice: str) -> None:
    """Handle user's menu choice."""
    if choice == "1":
        clearScreen()
        generateNewQRCode()
    elif choice == "2":
        clearScreen()
        decodeQRCode()
    elif choice == "3":
        sys.exit(0)
    else:
        print("\n\033[1;31mInvalid choice, please try again.\033[0m")
        input("Press Enter to continue...")
        main()


def main() -> None:
    """Main application entry point."""

    clearScreen()
    displayLogo()
    displayMenu()

    choice = input("Enter your choice (1-3): ")

    handleUserChoice(choice)


if __name__ == "__main__":
    while True:
        main()