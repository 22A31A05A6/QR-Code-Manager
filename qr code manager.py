import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import os

print("Secret Message Encoder/Decoder")
print("=================================")

while True:
    print("\n1. Encode a Message")
    print("2. Decode a Message")
    print("3. Exit")

    try:
        choice = int(input("Please enter your choice (1, 2, 3): "))

        if choice == 1:
            data = input("Enter the message to encode: ")
            qr = qrcode.make(data)
            filename = input("Enter filename to save QR code: ").strip()
            name, ext = os.path.splitext(filename)
            if ext.lower() != '.png':
                filename = name + '.png'

            qr.save(filename)
            print(f"QR Code saved as '{filename}'. Opening now...")
            qr.show()

        elif choice == 2:
            file_path = input("Enter the path to the QR Code image: ").strip().strip('"')
            name, ext = os.path.splitext(file_path)
            if ext.lower() != '.png':
                file_path = name + '.png'

            try:
                decoded = decode(Image.open(file_path))
                if decoded:
                    print("Decoded message:", decoded[0].data.decode('utf-8'))
                else:
                    print("No QR code found in the image.")
            except FileNotFoundError:
                print("File not found. Please check the file path.")

        elif choice == 3:
            print("Exiting the program.")
            break

        else:
            print("Please enter a valid option (1, 2, or 3).")

    except ValueError:
        print("Invalid input! Please enter a number.")
