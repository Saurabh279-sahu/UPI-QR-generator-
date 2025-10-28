

💰 UPI QR Generator (Python)

A simple and powerful Python script to generate payment-ready UPI QR codes that can be scanned directly by any UPI app — PhonePe, Paytm, Google Pay, BHIM, etc.
You can pre-fill payment details like amount and note message, then save the QR as an image.


---

🧩 Features

✅ Generate UPI QR instantly

💸 Pre-set payment amount and message

🖼️ Save QR code as JPG image

🔐 Works completely offline

⚡ Lightweight and fast



---

📁 Project File

upi_qr_generator.py


---

🛠️ Requirements

Python 3.7 or higher

Libraries:

qrcode[pil]

Pillow




---

⚙️ Installation

🟢 Termux / Linux
```bash
pkg update -y
pkg upgrade -y
pkg install python -y
pip install qrcode[pil]
```
🪟 Windows
```bash
pip install qrcode[pil]
```

---

▶️ How to Run

1. Save the file as upi_qr_v3.py


2. Run the script:
```bash
python upi_qr_generator.py
```

3. Enter your payment details when asked:
examle

Enter UPI ID: saurabh@paytm

Enter Payee Name: Saurabh Sahu

Enter Amount (₹): 150

Enter Note: Snacks Payment


5. The QR code will be generated and saved as:
``
upi_payment_qr.jpg
``

5. Open the image → Scan it using any UPI app to pay.




---

🧾 Example UPI Format
``
upi://pay?pa=saurabh@paytm&pn=Saurabh%20Sahu&am=150&tn=Snacks%20Payment
``

---

📸 Output Example

Example QR Image

(A black and white QR JPG file saved locally)



---

🚀 Coming Soon

Future update plans:

🪟 GUI Version (Tkinter): Generate and preview QR visually

📱 Android Build (Kivy): Create UPI QR from mobile

☁️ Online QR Tool: Convert directly via browser



---

✨ Author

Saurabh Sahu
Made with ❤️ in Python


---
