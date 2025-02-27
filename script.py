from PIL import Image, ImageDraw, ImageFont
from qr_generator import generate_qr
from util import details_to_file_name, date_to_str
import io

def add_line(image, content, font_file, font_size, color, y, x=None):
    """
    Adds a line to specified image object.
    """
    
    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Define font
    font = ImageFont.truetype(f"resources/{font_file}", font_size)  # Specify font and size

    # Define position and color
    # Dimensions 3509 x 2479

    if not x:
        text_width = draw.textlength(content, font=font)

        # Calculate x-coordinate for centering
        x = (image.width - text_width) // 2

    position = (x, y)

    # Add text to image
    draw.text(position, content, fill=color, font=font)

def add_text(image, name, course, date_created, date_issued):
    """
    Adding name and course to image.
    """
    
    # Take input and add name
    # print("Enter name: ", end = "") # Temporary CLI
    # name = input()
    
    processed_name = name.title().strip()

    add_line(
        image,
        content=processed_name,
        font_file="trebucbd.ttf",
        font_size=110,
        color=(0, 126, 201),
        y=990,
    )

    # Select course and add

    # courses = available_courses()
    # print("1.ReactJS\n2.Deep Learning for Developers\nSelect course: ", end = "")
    # course = int(input())

    add_line(
        image,
        content=course, # removed courses[course-1]
        font_file="trebucbd.ttf",
        font_size=78,
        color=(0, 126, 201),
        y=1310,
    )

    add_line(
        image,
        content=f"on {date_to_str(date_created)}",
        font_file="aptos.ttf",
        font_size=65,
        color=(0, 0, 0),
        y=1457,
    )

    add_line(
        image,
        content=f"Issued on: {date_issued.strftime("%A")}, {date_to_str(date_issued)}",
        font_file="aptos.ttf",
        font_size=40,
        color=(0, 0, 0),
        y=2253,
        x=130,
    )

def add_qr(image):
    """
    Adding QR.
    """
    
    overlay = generate_qr()

    # Open the overlay image
    overlay = overlay.convert("RGBA")
    alpha = 255
    overlay.putalpha(alpha)

    # Resize overlay if needed
    overlay = overlay.resize((735, 735))  # Adjust size as needed

    # Define position (x, y) for overlay
    position = (130, 1485)  # Top-left corner

    # Paste overlay image on the background (supports transparency)
    image.paste(overlay, position, overlay)

def generate_certificate(name, course, date_created, date_issued):
    """
    Main code for certificate generation.
    """
    
    # Open an image
    image = Image.open("resources/template.jpg")

    add_text(image, name, course, date_created, date_issued)

    add_qr(image)

    # Save the output image

    # image.save(f"output/output.jpg")
    # image.save(f"output/{details_to_file_name(name, course)}.pdf")

    # Create an in-memory bytes buffer
    pdf_buffer = io.BytesIO()

    # Save the image as a PDF in-memory
    image.save(pdf_buffer, format="PDF")

    # Move the pointer to the beginning of the buffer
    pdf_buffer.seek(0)

    return pdf_buffer  # This can be returned in a web response or saved externally
