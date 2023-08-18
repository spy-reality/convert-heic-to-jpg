from PIL import Image
import os
import pillow_heif

def convert_heic_to_jpg(input_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for root, _, files in os.walk(input_path):
        for filename in files:
            if filename.lower().endswith(".heic"):
                heic_path = os.path.join(root, filename)
                jpg_filename = os.path.splitext(filename)[0] + ".jpg"
                jpg_path = os.path.join(output_path, jpg_filename)

                try:
                    heif_file = pillow_heif.read_heif(heic_path)
                    img = Image.frombytes(
                        heif_file.mode,
                        heif_file.size,
                        heif_file.data,
                        "raw",
                    )
                    img.save(jpg_path, "JPEG")
                    print(f"Converted {heic_path} to {jpg_path}")
                except Exception as e:
                    print(f"Error converting {heic_path}: {e}")

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))

    input_folder = os.path.join(script_directory, ".")
    output_folder = os.path.join(script_directory, "convert")
    convert_heic_to_jpg(input_folder, output_folder)
