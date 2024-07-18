# Translator Application

This is a simple Translator application built using Python and Tkinter. It allows users to translate text from one language to another using the Translate Python module.

## Features

- Translate text between different languages.
- Clear text fields with a single button click.
- User-friendly interface with drop-down menus for language selection.
- Text area for input and output with automatic resizing.
- Handling of errors for language selection.

## Limitations
Arabic and any RTL langugages are not well displayed

## Working on

- Fix the issue with the Arabic language.
- Implement auto language detection.
- Add a favorite languages feature.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/translator-app.git
    ```

2. Navigate to the project directory:
    ```bash
    cd translator-app
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Install tkinter (Depends on your system)

## Usage

1. Run the application:
    ```bash
    python main.py
    ```

2. Select the source and target languages from the drop-down menus.

3. Enter the text you want to translate in the input text area.

4. Click the "Translate" button to see the translated text in the output text area.

5. Click the "Clear" button to clear both text fields.

## Code Overview

### `main.py`

The main file that sets up the Tkinter GUI and handles user interactions.

- **Text Entry 1**: For user input text.
- **Text Entry 2**: For displaying the translated text (read-only).
- **Translate Button**: Triggers the translation of text from the source language to the target language.
- **Clear Button**: Clears both text fields.
- **Language Dropdowns**: For selecting source and target languages.

### `myFunc.py`

Contains helper functions for the application:

- `translate_text(text_entry1, text_entry2, lang_dropdown1, lang_dropdown2)`: Translates the text from the source language to the target language.
- `clear_text(text_entry1, text_entry2)`: Clears both text fields.
- `clear(text_entry)`: Clears a specific text field.
- `languageSelectionException(src_lang, dest_lang)`: Handles errors related to language selection.

## Dependencies

- Python 3.x
- Tkinter
- googletrans==4.0.0-rc1 (or latest version)
- translate==3.6.1 (or latest version)

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

If you have any questions or suggestions, please feel free to contact me at `lyes.hadjar.04@gmail.com`

