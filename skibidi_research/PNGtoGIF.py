from PIL import Image
import os

def convert_png_to_gif(input_path, output_path):
    try:
        # Otwórz plik PNG
        img = Image.open(input_path)
        
        # PNG może zawierać przezroczystość, więc musimy sprawdzić, czy jest kanał alfa
        if img.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', img.size, (255, 255, 255))  # biały tło dla przezroczystych pikseli
            background.paste(img, mask=img.split()[3])  # Użyj kanału alfa jako maski
            img = background

        # Konwertuj do trybu P (który obsługuje format GIF)
        img = img.convert('P')

        # Zapisz jako plik GIF
        img.save(output_path, 'GIF')
        print(f'Successfully converted {input_path} to {output_path}')
    except Exception as e:
        print(f'Error: {e}')

# Ścieżka do pliku PNG
input_file = 'path_to_your_file/input_image.png'

# Ścieżka do wyjściowego pliku GIF
output_file = 'path_to_your_file/output_image.gif'

# Wywołanie funkcji konwersji
convert_png_to_gif(input_file, output_file)
