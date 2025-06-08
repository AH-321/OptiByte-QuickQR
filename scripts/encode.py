import os
import qrcode
from typing import NoReturn


def dirExists(directory: str) -> None:
    """Ensure the specified directory exists, creating it if necessary."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def generateQRCode(data: str, file_path: str) -> None:
    """Generate a QR code with the given data and save it to file_path."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)


def generateNewQRCode() -> NoReturn:
    """Generate a new QR code based on user input."""
    print("##### NEW ENTRY #####")
    encode_data = input("Enter name: ").strip()
    
    directory = "saved"
    dirExists(directory)
    
    code_file = os.path.join(directory, f"{encode_data}.png")
    if os.path.exists(code_file):
        print(f"QR code for '{encode_data}' already exists at '{code_file}'.")
        input("Press Enter to return to main menu...")
        return
    
    generateQRCode(encode_data, code_file)
    
    print(f"QR code generated and saved at '{code_file}'.")
    input("Press Enter to return to main menu...")  