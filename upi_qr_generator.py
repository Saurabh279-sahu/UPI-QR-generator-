import qrcode
import os
import datetime
from PIL import Image

# Folder path for saving QR code
save_folder = "/sdcard/UPI_QR"

# Create folder if not exists
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

print("=== 🏦 UPI QR Code Generator ===\n")

# Input details
name = input("Enter your name (optional): ") or "Unknown"
upi_id = input("Enter your UPI ID (e.g. name@upi): ").strip()
amount = input("Enter amount (leave blank for any amount): ").strip()
note = input("Enter payment note (optional): ") or "Payment"

# Build UPI URL
upi_url = f"upi://pay?pa={upi_id}&pn={name}&tn={note}"
if amount:
    upi_url += f"&am={amount}"

# Ask for custom filename or auto-generate using time
file_name = input("\nEnter QR file name (without extension): ").strip()
if not file_name:
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"UPI_{timestamp}"

file_path = os.path.join(save_folder, f"{file_name}.jpg")

# Generate QR code
qr = qrcode.make(upi_url)

# Convert to RGB (for JPG) and save
qr = qr.convert("RGB")
qr.save(file_path, "JPEG")

# Try to open file automatically (optional)
try:
    os.system(f"termux-open {file_path}")
except:
    pass

# Output
print("\n✅ QR code generated successfully!")
print(f"📂 Saved at: {file_path}")
print(f"🔗 UPI Link: {upi_url}")
