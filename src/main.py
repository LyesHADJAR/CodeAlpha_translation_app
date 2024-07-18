from tkinter import *
from tkinter import ttk
import tkinter as tk
from googletrans import LANGUAGES
from translation import translate_text, clear_text
from awesometkinter.bidirender import add_bidi_support

# =============================================================================
# TO DO:
# - Fix the issue with the Arabic language
# - Fix the Auto language detection
# - Brainstorm ideas to improve the app
# =============================================================================



# Function to clear text
def clear_text(text_entry1, text_entry2):
    text_entry1.delete("1.0", "end")
    text_entry2.delete("1.0", "end")

# App setting 
root = tk.Tk()
root.title("Translator")
root.geometry("1200x600")
root.resizable(False, False)

# Initial frame
frame1 = tk.Frame(root, width=1200, height=600, relief=RIDGE, borderwidth=0, bg="#000050")
frame1.place(x=0, y=0)

# Main title
Label(frame1, text="Translator", font=("Montserrat 30 bold"), bg="#000050", fg="white").place(x=490, y=10)

# Text entry 1 dimensions in pixels
text_entry1_width = 500
text_entry1_height = 250

# Text entry 2 dimensions in pixels
text_entry2_width = 500
text_entry2_height = 250

# Text entry 1
text_entry1 = tk.Text(frame1, font=("Montserrat 15"), bg="#EEEEEE", wrap=WORD)
text_entry1.place(x=50, y=150, width=text_entry1_width, height=text_entry1_height)

# Text entry 2
text_entry2 = tk.Text(frame1, font=("Montserrat 15"), bg="#EEEEEE", wrap=WORD)
text_entry2.place(x=650, y=150, width=text_entry2_width, height=text_entry2_height)

# Calculate positions to center buttons
button_width = 150
space_between_buttons = 20
total_width = button_width * 2 + space_between_buttons

# Translate Button
btn1 = tk.Button(frame1, text="Translate", font=("Montserrat", 15), bg="#ff5733", fg="white", borderwidth=0,
                 command=lambda: translate_text(text_entry1, text_entry2, lang_dropdown1, lang_dropdown2))
btn1.place(x=430, y=500, width=button_width)

# Clear Button
btn2 = tk.Button(frame1, text="Clear", font=("Montserrat", 15), bg="#ff3333", fg="white", borderwidth=0,
                 command=lambda: clear_text(text_entry1, text_entry2))
btn2.place(x=600, y=500, width=button_width)

# Language dropdown 1
language_list = [lang.capitalize() for lang in LANGUAGES.values()]
language_list.sort()
language_list.insert(0, "Auto")
lang_dropdown1 = ttk.Combobox(frame1, values=language_list, font=("Montserrat 15"), state="readonly")
lang_dropdown1.place(x=50, y=100, width=text_entry1_width, height=30)
lang_dropdown1.current(0)

# Language dropdown 2
lang_dropdown2 = ttk.Combobox(frame1, values=language_list, font=("Montserrat 15"), state="readonly")
lang_dropdown2.place(x=650, y=100, width=text_entry1_width, height=30)
lang_dropdown2.current(0)


# adding bidi support for widgets
add_bidi_support(text_entry1)
add_bidi_support(text_entry2)
add_bidi_support(lang_dropdown1)
add_bidi_support(lang_dropdown2)

root.mainloop()
