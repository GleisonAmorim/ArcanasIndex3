import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def select_folder(title):
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title=title)
    return folder_selected

def convert_images_to_jpeg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        if os.path.isfile(input_path):
            try:
                with Image.open(input_path) as img:
                    output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpeg")
                    img.convert("RGB").save(output_path, "JPEG")
                    print(f"Convertido: {filename} -> {output_path}")
            except Exception as e:
                print(f"Erro ao converter {filename}: {e}")

if __name__ == "__main__":
    input_folder = select_folder("Selecione a pasta com as imagens")
    if not input_folder:
        print("Nenhuma pasta selecionada. Saindo...")
        exit()
    
    output_folder = select_folder("Selecione a pasta onde serão salvos os arquivos convertidos")
    if not output_folder:
        print("Nenhuma pasta selecionada. Saindo...")
        exit()
    
    convert_images_to_jpeg(input_folder, output_folder)
    print("Conversão concluída!")
