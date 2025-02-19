import tkinter as tk
from tkinter import filedialog, StringVar
from tkinter.ttk import Style
from PIL import Image
import os

def apply_dark_mode():
    app.tk_setPalette(background='#2e2e2e', foreground='#f0f0f0', activeBackground='#4e4e2e', activeForeground='#f0f0f0')
    style = Style()
    style.configure('TButton', background='#4e4e4e', foreground='#f0f0f0')
    style.configure('TLabel', background='#2e2e2e', foreground='#f0f0f0')

def upload_photo():
    filepath = filedialog.askopenfilename(filetypes=[
        ("Image files", "*.png *.jpg *.jpeg *.webp *.bmp *.gif *.tiff *.ico *.jfif *.heic *.heif")
    ])
    if filepath:
        file_name.set(filepath)
        convert_button.config(state=tk.NORMAL)

def convert_photo():
    input_path = file_name.get()
    output_format = format_var.get()
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = filedialog.asksaveasfilename(defaultextension=f'.{output_format}', initialfile=f'{base_name}.{output_format}', filetypes=[(f'{output_format.upper()} files', f'*.{output_format}')])
    if output_path:
        img = Image.open(input_path)
        img.save(output_path, format=output_format.upper())

app = tk.Tk()
app.title("Image Converter")
app.geometry("400x200")

file_name = StringVar()
format_var = StringVar(value='png')

supported_types_label = tk.Label(app, text="Supported types: .png .jpg .jpeg .webp .bmp .gif .tiff .ico .jfif .heic .heif")
supported_types_label.pack(pady=10)

upload_button = tk.Button(app, text="Upload Photo", command=upload_photo)
upload_button.pack(pady=10)

file_label = tk.Label(app, textvariable=file_name)
file_label.pack(pady=10)

formats = ['png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif', 'tiff', 'ico', 'jfif', 'heic', 'heif']

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

convert_button = tk.Button(button_frame, text="Convert Photo", command=convert_photo, state=tk.DISABLED)
convert_button.pack(side=tk.LEFT, padx=5)

format_menu = tk.OptionMenu(button_frame, format_var, *formats)
format_menu.pack(side=tk.LEFT, padx=5)

apply_dark_mode()

app.mainloop()
