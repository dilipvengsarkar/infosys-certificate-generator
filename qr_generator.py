import qrcode
import uuid
import os

def generate_qr():
    """
    Generate new QR code.
    """

    if os.path.isfile("qr.jpg"):
        os.remove("qr.jpg")

    # Generate a random UUID-based string
    random_data = "https://verify.onwingspan.com/18efcp1" + str(uuid.uuid4())  # Example: "f47ac10b-58cc-4372-a567-0e02b2c3d479"

    # Create a QR code object
    qr = qrcode.QRCode(
        version=20,  # Controls size (1 to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # L (low), M, Q, H (high)
        box_size=10,  # Size of each box in pixels
        border=1  # Border thickness
    )

    # Add data to QR code
    qr.add_data(random_data)
    qr.make(fit=True)

    # Generate QR code image
    img = qr.make_image(fill="black", back_color="white")

    # Save or display
    img.save("qr.jpg")  # Save as image
