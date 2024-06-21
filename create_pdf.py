from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def create_pdf(png_files, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=A4)
    (w, h) = A4  # A4 size in points (1 point = 1/72 inch)
    
    for png_file in png_files:
        # Open the image
        img = Image.open(png_file)
        
        # Check if image needs to be resized to fit A4
        img_width, img_height = img.size
        aspect = img_height / float(img_width)
        if img_width > w or img_height > h:
            if img_width / w > img_height / h:
                img_width = w
                img_height = w * aspect
            else:
                img_height = h
                img_width = h / aspect
        
        # Position the image in the center of the page
        x = (w - img_width) / 2
        y = (h - img_height) / 2
        
        # Draw the image
        c.drawImage(png_file, x, y, img_width, img_height)
        c.showPage()  # Add a new page for the next image

    c.save()

# List of PNG files in order
png_files = [
    'image1.png',
    'image2.png',
    'image3.png',
    'image4.png',
    'image5.png',
    'image6.png',
    'image7.png',
    'image8.png',
    'image9.png',
    'image10.png',
    'image11.png'
]

# Output PDF file
NDA = "output.pdf"

# Create PDF
create_pdf(png_files, NDA)

print(f"PDF created successfully: {NDA}")
