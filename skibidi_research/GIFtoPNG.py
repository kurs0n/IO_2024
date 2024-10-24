from PIL import Image
import os

def convert_gif_to_png(input_path, output_path):
    try:
        # Otwórz plik GIF
        img = Image.open(input_path)

        # Sprawdź, czy GIF jest animowany, i wybierz pierwszą klatkę, jeśli tak
        img.seek(0)  # Ustaw na pierwszą klatkę (jeśli animowany)
        
        # Konwertuj obraz do formatu PNG i zapisz
        img.save(output_path, 'PNG')
        print(f'Successfully converted {input_path} to {output_path}')
    except Exception as e:
        print(f'Error: {e}')

# Ścieżka do pliku GIF
input_file = 'path_to_your_file/input_image.gif'

# Ścieżka do wyjściowego pliku PNG
output_file = 'path_to_your_file/output_image.png'

# Wywołanie funkcji konwersji
convert_gif_to_png(input_file, output_file)
