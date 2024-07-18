from translate import Translator
from googletrans import LANGUAGES

# Function to translate text
def translate_text(text_entry1, text_entry2, lang_dropdown1, lang_dropdown2):
    src_lang = lang_dropdown1.get()
    dest_lang = lang_dropdown2.get()
    
    if src_lang == "Auto":
        src_lang = 'auto'
        
    else:
        src_lang = [key for key, value in LANGUAGES.items() if value == src_lang.lower()][0]
    
    dest_lang = [key for key, value in LANGUAGES.items() if value == dest_lang.lower()][0]
    
    if src_lang == 'arabic' or dest_lang == 'arabic':
        translator = Translator(from_lang=src_lang, to_lang=dest_lang)
        translation = translator.translate(text_entry1.get("1.0", "end-1c"))
        text_entry2.delete("1.0", "end")
        text_entry2.insert("1.0", translation)
        
    translator = Translator(from_lang=src_lang, to_lang=dest_lang)
    translation = translator.translate(text_entry1.get("1.0", "end-1c"))
    text_entry2.delete("1.0", "end")
    text_entry2.insert("1.0", translation)

# Function to clear text
def clear_text(text_entry1, text_entry2):
    text_entry1.delete("1.0", "end")
    text_entry2.delete("1.0", "end")
