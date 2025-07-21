import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import os

print("Secret Message Encoder/Decoder ")
print("=" * 35)

while True:
    print("\nChoose an option:")
    print("1 → Encode a message into QR")
    print("2 → Decode a QR to read message")
    print("3 → Exit")

    try:
        choice = int(input("Your pick (1/2/3): "))

        if choice == 1:
            message = input("Type your secret message: ")
            qr_image = qrcode.make(message)

            filename = input("Filename to save as (.png auto-added if missing): ").strip()
            name, ext = os.path.splitext(filename)
            if ext.lower() != '.png':
                filename = name + '.png'

            qr_image.save(filename)
            print(f"Saved QR code as '{filename}'. Opening...")
            qr_image.show()

        elif choice == 2:
            path = input("Path to QR image file: ").strip().strip('"')
            name, ext = os.path.splitext(path)
            if ext.lower() != '.png':
                path = name + '.png'

            try:
                decoded_data = decode(Image.open(path))
                if decoded_data:
                    print("Decoded Message:", decoded_data[0].data.decode('utf-8'))
                else:
                    print("No QR code detected in the image.")
            except FileNotFoundError:
                print("File not found. Double-check the path.")

        elif choice == 3:
            print("Goodbye! Stay encrypted.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    except ValueError:
        print("Error: Please enter a number.")
