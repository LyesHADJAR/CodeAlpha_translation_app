from tkinter import *
from tkinter import ttk
import tkinter as tk
from googletrans import LANGUAGES
from myFunc import translate_text, clear_text

# ==========================================================================================================================================================
# TO DO:
# - Fix the issue with the Arabic language                                (TBD LATER)
# - Fix the Auto language detection                                       (TBD LATER)
# - Brainstorm ideas to improve the app                                   (TBD LATER)
# - Add a feature to detect the language of the input text                (TBD LATER)
# - Add a favourite languages feature                                     (TBD LATER)
# - Make outputText readonly                                              (DONE)
# ==========================================================================================================================================================


# App setting 
root = tk.Tk()
root.title("Translator")
root.geometry("1200x600")
root.resizable(False, False)

# Initial frame
frame1 = tk.Frame(root, width=1200, height=600, relief=RIDGE, borderwidth=0, bg="#000050")
frame1.place(x=0, y=0)

# Main title
lbl = Label(frame1, text="Translator", font=("Montserrat 30 bold"), bg="#000050", fg="white")
lbl.place(x=490, y=10)

# Text entry dimensions in pixels
text_entry_width = 500
text_entry_height = 250

# Text entry 1
entryText = tk.Text(frame1, font=("Montserrat 15"), bg="#EEEEEE", wrap=WORD)
entryText.place(x=50, y=150, width=text_entry_width, height=text_entry_height)

# Text entry 2
outputText = tk.Text(frame1, font=("Montserrat 15"), bg="#EEEEEE", wrap=WORD)
outputText.place(x=650, y=150, width=text_entry_width, height=text_entry_height)
outputText.config(state=tk.DISABLED)

# Calculate positions to center buttons
button_width = 150
space_between_buttons = 20
total_width = button_width * 2 + space_between_buttons

# Translate Button
translateButton = tk.Button(frame1, text="Translate", font=("Montserrat", 15), bg="#ff5733", fg="white", borderwidth=0,
                 command=lambda: translate_text(entryText, outputText, sourceLang, targetLang))
translateButton.place(x=430, y=500, width=button_width)

# Clear Button
clearButton = tk.Button(frame1, text="Clear", font=("Montserrat", 15), bg="#ff3333", fg="white", borderwidth=0,
                 command=lambda: clear_text(entryText, outputText))
clearButton.place(x=600, y=500, width=button_width)

# List of languages
language_list = [lang.capitalize() for lang in LANGUAGES.values()]
language_list.sort()
language_list.insert(0, "Select a Language ...")

# Language dropdown 1
sourceLang = ttk.Combobox(frame1, values=language_list, font=("Montserrat 15"), state="readonly")
sourceLang.place(x=50, y=100, width=text_entry_width, height=30)
sourceLang.current(0)

# Language dropdown 2
targetLang = ttk.Combobox(frame1, values=language_list, font=("Montserrat 15"), state="readonly")
targetLang.place(x=650, y=100, width=text_entry_width, height=30)
targetLang.current(0)

# Run the app
root.mainloop()
