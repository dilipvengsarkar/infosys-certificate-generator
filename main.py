from PIL import Image, ImageDraw, ImageFont
from qr_generator import generate_qr

def add_name(image, name, y, font_size):
    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Define font
    font = ImageFont.truetype("trebucbd.ttf", font_size)  # Specify font and size

    # Define position and color
    # Dimensions 3509 x 2479

    text_width = draw.textlength(name, font=font)

    # Calculate x-coordinate for centering
    x = (image.width - text_width) // 2
    position = (x, y)

    color = (0, 126, 201) # Blue color

    # Add text to image
    draw.text(position, name, fill=color, font=font)

def add_text(image):
    """
    Adding name and course to image.
    """
    
    # Take input and add name
    print("Enter name: ", end = "") # Temporary CLI
    name = input()
    res = name.title().strip()

    add_name(image, res, 990, 110)

    # Select course and add
    courses = ("ReactJS", "Deep Learning for Developers")
    print("1.ReactJS\n2.Deep Learning for Developers\nSelect course: ", end = "")
    course = int(input())

    add_name(image, courses[course-1], 1310, 78)

def add_qr(image):
    """
    Adding QR.
    """
    
    generate_qr()

    # Open the overlay image
    overlay = Image.open("qr.jpg")

    overlay = overlay.convert("RGBA")
    alpha = 255
    overlay.putalpha(alpha)

    # Resize overlay if needed
    overlay = overlay.resize((735, 735))  # Adjust size as needed

    # Define position (x, y) for overlay
    position = (130, 1485)  # Top-left corner

    # Paste overlay image on the background (supports transparency)
    image.paste(overlay, position, overlay)

def main():
    # Open an image
    image = Image.open("template.jpg")

    add_text(image)

    add_qr(image)

    # Save the output image
    image.save("output.jpg")

if __name__ == "__main__":
    main()
