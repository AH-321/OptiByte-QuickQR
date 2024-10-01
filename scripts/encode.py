import os
import qrcode

if os.name == 'nt':
    python_interpreter = '.venv\\Scripts\\python.exe'
else:
    python_interpreter = '.venv/bin/python'

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

def new_entry():
    print("#####NEW ENTRY#####")
    encode_data = input("Enter name:")
    directory = "saved"
    if not os.path.exists(directory):
        os.makedirs(directory)
    code_file = os.path.join(directory, encode_data + ".png")
    generate_qr_code(encode_data, code_file)
    print(f"QR code generated and saved as {code_file}")

    os.system(f'{python_interpreter} QuickQR.py')

new_entry()
