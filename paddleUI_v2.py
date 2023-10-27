import tkinter as tk
from tkinter import filedialog, Text
from tkinterdnd2 import DND_FILES, TkinterDnD
import customtkinter as ctk
from tkinter import ttk
import threading
from paddleocr import PaddleOCR
import numpy as np
from tkinter_webcam import webcam
import cv2


"""
TO DO:
# ! 
"""

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

BG_COLOR = "#2b2b2b"
FG_COLOR = "#ffffff"
SELECT_BG = "#555555"

class TopLevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        screen_pos_x = App.winfo_rootx(self)
        screen_pos_y = App.winfo_rooty(self)
        pos_x = (screen_pos_x * 2) - (200 / 2)
        pos_y = (screen_pos_y * 2) - (50 / 2)
        self.geometry("400x50+%d+%d" % (pos_x, pos_y))
        self.progressbar = ctk.CTkProgressBar(self)
        self.progressbar.grid(row=0, column=0, padx=10, pady=(0,0), sticky="new")
        #self.progressbar.place(relx=0.5, rely=0.5, anchor="center")
        self.overrideredirect(True)
        self.button = ctk.CTkButton(self, text="Cancel", command=self.stop)
        self.button.grid(row=1, column=0, padx=10, pady=(0,0), sticky="s")
        
    def start(self):
        self.progressbar.start()   

    def stop(self):
        self.progressbar.stop()

class CameraFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.webcam_object = webcam.Box(self)
        self.webcam_object.show_frames()
        

class TopFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # TAB
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        self.tabview.add("Select File")
        self.tabview.add("Camera")
        self.tabview.set("Select File")
        # INPUT BOX
        self.listbox = tk.Listbox(self.tabview.tab("Select File"), selectmode=tk.SINGLE, bg=BG_COLOR, fg=FG_COLOR, selectbackground=SELECT_BG)
        self.listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        self.isCamConnected = False
        self.testDevice(0)
        self.cap = cv2.VideoCapture(0)

        if (self.isCamConnected):
            self.open_cv_frame = CameraFrame(self.tabview.tab("Camera"))
            self.open_cv_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        else:
            self.open_cv_frame = ctk.CTkLabel(self.tabview.tab("Camera"), text="No camera detected!")
            self.open_cv_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    def testDevice(self, source):
        cap = cv2.VideoCapture(0)
        if cap is None or not cap.isOpened():
            print('Warning: unable to open video source', source)
            return self.isCamConnected
        else:
            self.isCamConnected = True
    
    def show_list(selected_option):
        print()

    def add_to_list(self, idx, name):
        print()


class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


class OutputFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # OUTPUT BOX
        self.textbox = Text(self, wrap=tk.WORD, bg=BG_COLOR, fg=FG_COLOR, selectbackground=SELECT_BG)
        self.textbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # WINDOW
        self.title('PaddleOCR GUI')
        self.geometry('600x600')
        self.grid_columnconfigure((0,3), weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.configure(bg=BG_COLOR)

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # TOP FRAME
        self.top_frame = TopFrame(self)
        self.top_frame.grid(row=0, column=0, columnspan=4, padx=20, pady=(20,0), sticky="new")

        # BUTTON FRAME
        self.button_frame = ButtonFrame(self)
        self.button_frame.grid(row=1, column=0, columnspan=4, padx=0, pady=(0,0), sticky="ew")
        
        # BUTTONS
        self.btn_add = ctk.CTkButton(self.button_frame, text="Add Files", bg_color=BG_COLOR, border_color=BG_COLOR, command=self.add_files)
        self.btn_add.grid(row=1, column=0, padx=5, pady=(10,0))

        self.btn_clear = ctk.CTkButton(self.button_frame, text="Clear", bg_color=BG_COLOR, border_color=BG_COLOR, command=self.clear_selection)
        self.btn_clear.grid(row=1, column=1, padx=5, pady=(10,0))

        self.btn_clear_all = ctk.CTkButton(self.button_frame, text="Clear All", bg_color=BG_COLOR, border_color=BG_COLOR, command=self.clear_all)
        self.btn_clear_all.grid(row=1, column=2, padx=5, pady=(10,0))

        self.btn_transcribe = ctk.CTkButton(self.button_frame, text="Transcribe", bg_color=BG_COLOR, border_color=BG_COLOR, command=self.transcribe_file)
        self.btn_transcribe.grid(row=1, column=3, padx=5, pady=(10,0))

        # OUTPUT FRAME
        self.output_frame = OutputFrame(self)
        self.output_frame.grid(row=2, column=0, columnspan=4, padx=0, pady=(0,0), sticky="sew")

        # PROGRESS BAR
        self.progress_bar_window = None

        # Load Model
        self.load_model()
    
    def load_model(self):
        #self.open_progress_bar()
        #self.progress_bar_window.start()
        self.ocr_model = PaddleOCR(use_angle_cls=True, lang='en')
        #self.progress_bar_window.stop()

    
    def add_files(self):
        files = filedialog.askopenfilenames()
        for f in files:
            self.top_frame.listbox.insert(tk.END, f)

    def clear_selection(self):
        selected = self.top_frame.listbox.curselection()
        for index in reversed(selected):
            self.top_frame.listbox.delete(index)

    def clear_all(self):
        self.top_frame.listbox.delete(0, tk.END)

    def transcribe_file(self):
        if self.top_frame.listbox.curselection():
            #self.progress_bar_window.start()
            def transcribe():
                selected_item = self.top_frame.listbox.get(self.top_frame.listbox.curselection())
                result = self.ocr_model.ocr(selected_item, cls=True)
                self.output_frame.textbox.delete('1.0', tk.END)
                for x, res in enumerate(result[0]):
                    self.output_frame.textbox.insert(tk.END, result[0][x][1][0])
                    self.output_frame.textbox.insert(tk.END, "\n")
                self.output_frame.textbox.clipboard_clear()
                self.output_frame.textbox.clipboard_append(self.output_frame.textbox.get('1.0', tk.END))

            thread = threading.Thread(target=transcribe)
            thread.start()
            
            #self.progress_bar_window.stop()
        else:
            self.output_frame.textbox.delete(1.0, tk.END)
            self.output_frame.textbox.insert(tk.END, "Select an item to transcribe")


    def open_progress_bar(self):
        if self.progress_bar_window is None or not self.progress_bar_window.winfo_exists():
            # create window if its None or destroyed
            self.progress_bar_window = TopLevelWindow(self)
        else:
            # if window exists focus it
            self.progress_bar_window.focus()
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
