from PIL import Image
import os

def convert_jpg_to_png(input_path, output_path):
    try:
        # Otwórz plik JPG
        img = Image.open(input_path)
        # Zapisz obraz w formacie PNG
        img.save(output_path, 'PNG')
        print(f'Successfully converted {input_path} to {output_path}')
    except Exception as e:
        print(f'Error: {e}')

# Ścieżka do pliku JPG
input_file = 'path_to_your_file/input_image.jpg'

# Ścieżka do wyjściowego pliku PNG
output_file = 'path_to_your_file/output_image.png'

# Wywołanie funkcji konwersji
convert_jpg_to_png(input_file, output_file)
