from PIL import Image
import os

def convert_jpg_to_gif(input_path, output_path):
    try:
        # Otwórz plik JPG
        img = Image.open(input_path)
        
        # Konwertuj do trybu RGB na tryb P (który obsługuje format GIF)
        img = img.convert('P')

        # Zapisz jako plik GIF
        img.save(output_path, 'GIF')
        print(f'Successfully converted {input_path} to {output_path}')
    except Exception as e:
        print(f'Error: {e}')

# Ścieżka do pliku JPG
input_file = 'path_to_your_file/input_image.jpg'

# Ścieżka do wyjściowego pliku GIF
output_file = 'path_to_your_file/output_image.gif'

# Wywołanie funkcji konwersji
convert_jpg_to_gif(input_file, output_file)
