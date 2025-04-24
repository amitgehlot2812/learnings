import qrcode
import os

def qrcode_generator():
    try:
        user_data = input('Enter your link:\n➤ ').strip()
        if not user_data:
            raise ValueError("Link cannot be empty.")

        user_filename = input('Enter the file name (without extension):\n➤ ').strip()
        if not user_filename:
            raise ValueError("Filename cannot be empty.")

        if not user_filename.lower().endswith('.png'):
            user_filename += '.png'

        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )
        qr.add_data(user_data)
        qr.make(fit=True)

        image = qr.make_image(fill_color="black", back_color="white")
        image.save(user_filename)

        print(f'✅ QR Code saved as "{os.path.abspath(user_filename)}"')

    except ValueError as ve:
        print(f"❗ Input Error: {ve}")

    except Exception as e:
        print(f"❗ Unexpected error occurred: {e}")

qrcode_generator()