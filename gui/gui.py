import subprocess
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_to_purestatus_format(input_file, output_file):
    try:
        if not os.path.exists(input_file):
            messagebox.showerror("Error", f"Input file '{input_file}' tidak ditemukan.")
            return
        
        command = [
            "ffmpeg",
            "-i", input_file,
            "-vf", "scale=1080:1920",
            "-r", "59.94",
            "-b:v", "5M",
            "-c:v", "libx264",
            "-preset", "medium",
            "-c:a", "aac",
            "-b:a", "128k",
            "-strict", "experimental",
            output_file
        ]
        
        subprocess.run(command, check=True)
        messagebox.showinfo("Sukses", f"Konversi berhasil! Disimpan sebagai '{output_file}'.")

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat konversi: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Kesalahan tidak terduga: {e}")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mov;*.mp4")])
    if file_path:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, file_path)

def select_output():
    output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 Files", "*.mp4")])
    if output_path:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, output_path)

def start_conversion():
    input_file = entry_input.get()
    output_file = entry_output.get()
    if input_file and output_file:
        convert_to_purestatus_format(input_file, output_file)
    else:
        messagebox.showwarning("Warning", "Harap pilih file input dan output.")

# GUI Setup
root = tk.Tk()
root.title("Video Converter")

tk.Label(root, text="Pilih Video Input:").grid(row=0, column=0, padx=10, pady=5)
entry_input = tk.Entry(root, width=50)
entry_input.grid(row=0, column=1, padx=10, pady=5)
btn_input = tk.Button(root, text="Browse", command=select_file)
btn_input.grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Pilih Output File:").grid(row=1, column=0, padx=10, pady=5)
entry_output = tk.Entry(root, width=50)
entry_output.grid(row=1, column=1, padx=10, pady=5)
btn_output = tk.Button(root, text="Browse", command=select_output)
btn_output.grid(row=1, column=2, padx=10, pady=5)

btn_convert = tk.Button(root, text="Convert", command=start_conversion)
btn_convert.grid(row=2, column=1, padx=10, pady=20)

root.mainloop()
