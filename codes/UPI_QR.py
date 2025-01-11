import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image

# Function to generate QR code for a specific payment URL
def generate_qr():
    try:
        data = entry.get()
        if not data:
            messagebox.showerror("Input Error", "Please enter the data (UPI ID or Payment URL).")
            return

        # Check which service user selected
        service = service_var.get()
        
        if service == 'PhonePe':
            # Format URL for PhonePe
            qr_data = f"phonepe://pay?pa={data}&pn=YourName&mc=YourMerchantCode&tid=123456&tr=TX12345&tn=PaymentNote&am=100&cu=INR"
        elif service == 'Google Pay':
            # Format URL for Google Pay
            qr_data = f"https://pay.google.com/gp/p/ui/pay?pa={data}&pn=YourName&mc=YourMerchantCode&tid=123456&tr=TX12345&tn=PaymentNote&am=100&cu=INR"
        elif service == 'Paytm':
            # Format URL for Paytm
            qr_data = f"paytm://pay?pa={data}&pn=YourName&mc=YourMerchantCode&tid=123456&tr=TX12345&tn=PaymentNote&am=100&cu=INR"
        else:
            messagebox.showerror("Input Error", "Please select a payment service.")
            return
        


        # Create the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Create image from QR code
        img = qr.make_image(fill='black', back_color='white')

        # Convert image for Tkinter
        img_tk = ImageTk.PhotoImage(img)

        # Update the label to display the QR code
        qr_code_label.config(image=img_tk)
        qr_code_label.image = img_tk
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")



# Create main window
root = tk.Tk()
root.title("Payment QR Code Generator")

# Create Entry widget for user input (e.g., UPI ID or Payment Address)
entry_label = tk.Label(root, text="Enter UPI ID or Payment Address:")
entry_label.pack(padx=10, pady=5)

entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)

# Create Radio buttons for selecting the payment service
service_var = tk.StringVar(value="PhonePe")

radio_button_phonepe = tk.Radiobutton(root, text="PhonePe", variable=service_var, value="PhonePe")
radio_button_phonepe.pack(anchor="w", padx=10)

radio_button_gpay = tk.Radiobutton(root, text="Google Pay", variable=service_var, value="Google Pay")
radio_button_gpay.pack(anchor="w", padx=10)

radio_button_paytm = tk.Radiobutton(root, text="Paytm", variable=service_var, value="Paytm")
radio_button_paytm.pack(anchor="w", padx=10)

# Create Generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# Label to display the QR code image
qr_code_label = tk.Label(root)
qr_code_label.pack(pady=10)

# Run the GUI loop
root.mainloop()

