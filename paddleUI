import tkinter as tk
from tkinter import filedialog, Text
from tkinterdnd2 import DND_FILES, TkinterDnD
import customtkinter as ctk
from tkinter import ttk
import threading
from paddleocr import PaddleOCR

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

BG_COLOR = "#2b2b2b"
FG_COLOR = "#ffffff"
SELECT_BG = "#555555"

def drop(event):
    files = event.data.strip().split()
    for f in files:
        listbox.insert(tk.END, f)

def add_files():
    files = filedialog.askopenfilenames()
    for f in files:
        listbox.insert(tk.END, f)

def clear_selection():
    selected = listbox.curselection()
    for index in reversed(selected):
        listbox.delete(index)

def clear_all():
    listbox.delete(0, tk.END)

def transcribe_file():
    # In the future, your transcribe function will go here
    if listbox.curselection():
        progress_window = tk.Toplevel(root)
        progress_window.title(" ")
        screen_width = progress_window.winfo_screenwidth()
        screen_height = progress_window.winfo_screenheight()

        x_pos = (screen_width / 2) - (200 / 2)
        y_pos = (screen_height / 2) - (50 / 2)

        progress_window.geometry("400x50+%d+%d" % (x_pos, y_pos))
        progressbar = ttk.Progressbar(progress_window, orient="horizontal", length=400, mode="indeterminate")
        progressbar.pack()
        progressbar.start()
        progress_window.update()

        def transcribe():
            selected_item = listbox.get(listbox.curselection())
            result = ocr_model.ocr(selected_item, cls=True)
            textbox.delete('1.0', tk.END)
            for x, res in enumerate(result[0]):
                textbox.insert(tk.END, result[0][x][1][0])
                textbox.insert(tk.END, "\n")
            textbox.clipboard_clear()
            textbox.clipboard_append(textbox.get('1.0', tk.END))
            progressbar.stop()
            progress_window.destroy()

        thread = threading.Thread(target=transcribe)
        thread.start()

    else:
        textbox.delete(1.0, tk.END)
        textbox.insert(tk.END, "Select an item to transcribe")

root = TkinterDnD.Tk()
root.geometry('600x600')
root.title('PaddleOCR GUI')
root.configure(bg=BG_COLOR)

# File listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE, bg=BG_COLOR, fg=FG_COLOR, selectbackground=SELECT_BG)
listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
listbox.drop_target_register(DND_FILES)
listbox.dnd_bind('<<Drop>>', drop)

# Buttons
btn_frame = ctk.CTkFrame(root)
btn_frame.pack(pady=20, padx=20, fill=tk.X)

btn_add = ctk.CTkButton(btn_frame, text="Add Files", bg_color=BG_COLOR, border_color=BG_COLOR, command=add_files)
btn_add.pack(side=tk.LEFT, padx=1)

btn_clear = ctk.CTkButton(btn_frame, text="Clear", bg_color=BG_COLOR, border_color=BG_COLOR, command=clear_selection)
btn_clear.pack(side=tk.LEFT, padx=1)

btn_clear_all = ctk.CTkButton(btn_frame, text="Clear All", bg_color=BG_COLOR, border_color=BG_COLOR, command=clear_all)
btn_clear_all.pack(side=tk.LEFT, padx=1)

btn_transcribe = ctk.CTkButton(btn_frame, text="Transcribe", bg_color=BG_COLOR, border_color=BG_COLOR, command=transcribe_file)
btn_transcribe.pack(side=tk.LEFT, padx=1)

# Textbox for transcribe output
textbox = Text(root, wrap=tk.WORD, bg=BG_COLOR, fg=FG_COLOR, selectbackground=SELECT_BG)
textbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

ocr_model = PaddleOCR(use_angle_cls=True, lang='en')

root.mainloop()
