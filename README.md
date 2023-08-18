# HEIC to JPG Converter

This is a Python script that converts HEIC files to JPG format using the PIL (Python Imaging Library) and pillow-heif library.

## Requirements

- Python 3.x <a href="https://www.python.org/downloads/" target="_blank">Download</a>
- PIL (Python Imaging Library)
- pillow-heif

On Windows, you can open the Command Prompt (CMD) by following these steps:

- Press Windows Key + R to open the Run dialog.
- Type cmd and press Enter.
- Then, run the following pip command.

You can install the required libraries using the following command:

```bash
pip install pillow pillow-heif
```

## Usage

1. Clone this repository:
   
   ```bash
   git clone https://github.com/spy-reality/convert-heic-to-jpg.git

   cd convert-heic-to-jpg
   ```

2. Place your HEIC files in the folder.<br>

3. Run the script:

   ```python
   python convert_heic_to_jpg.py
   ```

   <small>`On Windows, you can double-click the convert_heic_to_jpg.py file to run it.`</small>

   The converted JPG files will be saved in the convert folder.

## Note

- Make sure to keep the script and your HEIC files in the same directory.
- The script will create the convert folder if it doesn't exist.
- If you encounter any issues during conversion, please check the error messages and ensure that the required libraries are installed.

## License
This project is licensed under the MIT License.
