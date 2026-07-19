import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("DisasterEye AI")
app.geometry("800x600")
heading = ctk.CTkLabel(app, text="DisasterEye AI - Disaster Image Analyzer", font=("Arial", 20))
heading.pack(pady=20)

preview_label = ctk.CTkLabel(app, text="", width=400, height=300, fg_color="gray20")
preview_label.pack(pady=10)

analyze_btn = ctk.CTkButton(app, text="Analyze", state="disabled")
analyze_btn.pack(pady=10)

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((400, 300))
        ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=img.size)
        preview_label.configure(image=ctk_img, text="")
        analyze_btn.configure(state="normal")

upload_btn = ctk.CTkButton(app, text="Upload Image", command=upload_image)
upload_btn.pack(pady=10)

app.mainloop()