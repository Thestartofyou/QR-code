import qrcode

# Set the data you want to encode as a QR code
data = "Hello, world!"

# Create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Add data to the QR code instance
qr.add_data(data)

# Generate the QR code as an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image as a PNG file
img.save("qrcode.png")

