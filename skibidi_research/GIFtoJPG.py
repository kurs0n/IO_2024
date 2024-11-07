from PIL import Image
import os

def convert_gif_to_jpg(input_path, output_path):
    try:
        # Otwórz plik GIF
        img = Image.open(input_path)

        # GIF może być animowany, więc wyciągamy pierwszą klatkę
        img = img.convert('RGB')  # Konwertujemy do trybu RGB (JPG nie obsługuje przezroczystości)

        # Zapisz jako plik JPG
        img.save(output_path, 'JPEG')
        print(f'Successfully converted {input_path} to {output_path}')
    except Exception as e:
        print(f'Error: {e}')

# Ścieżka do pliku GIF
input_file = 'path_to_your_file/input_image.gif'

# Ścieżka do wyjściowego pliku JPG
output_file = 'path_to_your_file/output_image.jpg'

# Wywołanie funkcji konwersji
convert_gif_to_jpg(input_file, output_file)
