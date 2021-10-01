import os
import qrcode
# Generate QR code
img = qrcode.make("your link here which you want to make qr"
)
# Save as file
img.save("qrcode.png", "PNG"
)
# Open file 
os.system("open qrcode.png"
)
