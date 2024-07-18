from translate import Translator
import tkinter as tk
from googletrans import LANGUAGES
from tkinter import messagebox


# Clear a text widget
def clear(text_entry):
    text_entry.delete("1.0", "end")

# Function to translate text
def translate_text(text_entry1, text_entry2, lang_dropdown1, lang_dropdown2):
    
    src_lang = lang_dropdown1.get()
    dest_lang = lang_dropdown2.get()
    
    if(not src_lang == "Select a Language ..." and not dest_lang == "Select a Language ..."):
        
        src_lang = [key for key, value in LANGUAGES.items() if value == src_lang.lower()][0]
        dest_lang = [key for key, value in LANGUAGES.items() if value == dest_lang.lower()][0]
        
        translator = Translator(from_lang=src_lang, to_lang=dest_lang)
        translation = translator.translate(text_entry1.get("1.0", "end-1c"))
        
        text_entry2.config(state=tk.NORMAL)
        clear(text_entry2)
        text_entry2.insert("1.0", translation)
        text_entry2.config(state=tk.DISABLED)
    
    else:    
        languageSelectionException(src_lang, dest_lang)
    
# No Selected Language Handling
def languageSelectionException(src_lang, dest_lang):
    if(src_lang == "Select a Language ..." and dest_lang == "Select a Language ..."):
        messagebox.showerror("Error", "Please select both source and target languages ...")
        return
    elif(src_lang == "Select a Language ..." and not dest_lang == "Select a Language ..."):
        messagebox.showerror("Error", "Please select a source languages ...")
        return
    elif(not src_lang == "Select a Language ..." and  dest_lang == "Select a Language ..."):
        messagebox.showerror("Error", "Please select a target languages ...")
        return
    
    
# Function to clear all text fields
def clear_text(text_entry1, text_entry2):
    clear(text_entry1)
    text_entry2.config(state=tk.NORMAL)
    clear(text_entry2)
    text_entry2.config(state=tk.DISABLED)
