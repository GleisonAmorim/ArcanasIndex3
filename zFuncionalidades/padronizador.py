from PIL import Image
import os
from tkinter import filedialog, Tk

def colar_imagem_no_centro(imagem_fundo, pasta_imagens, pasta_saida, fator_redimensionamento=0.3):
    # Abrindo a imagem de fundo (modo paisagem)
    fundo = Image.open(imagem_fundo)

    # Criar a pasta de saída caso não exista
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Listar todas as imagens da pasta
    imagens_para_colar = [f for f in os.listdir(pasta_imagens) if f.lower().endswith(('jpg', 'jpeg', 'png'))]

    for imagem_nome in imagens_para_colar:
        # Abrir a imagem que vai ser colada no centro
        imagem = Image.open(os.path.join(pasta_imagens, imagem_nome))

        # Redimensionar a imagem para que ela caiba no fundo (aplicar um fator de redimensionamento)
        largura_fundo, altura_fundo = fundo.size
        largura_imagem, altura_imagem = imagem.size

        # Calcular o tamanho proporcional baseado no fator de redimensionamento
        nova_largura = int(largura_fundo * fator_redimensionamento)
        nova_altura = int(altura_imagem * (nova_largura / largura_imagem))  # Mantendo a proporção

        # Redimensionar a imagem
        imagem_redimensionada = imagem.resize((nova_largura, nova_altura))

        # Calcular as coordenadas para colar a imagem no centro da imagem de fundo
        largura_imagem_redimensionada, altura_imagem_redimensionada = imagem_redimensionada.size
        x = (largura_fundo - largura_imagem_redimensionada) // 2
        y = (altura_fundo - altura_imagem_redimensionada) // 2

        # Colar a imagem no fundo
        fundo_copy = fundo.copy()
        fundo_copy.paste(imagem_redimensionada, (x, y))

        # Salvar a nova imagem
        novo_nome = os.path.join(pasta_saida, f"{imagem_nome}")
        fundo_copy.save(novo_nome)

    print(f"Imagens salvas na pasta: {pasta_saida}")

def selecionar_imagens():
    # Configuração da interface para selecionar os arquivos e pasta
    root = Tk()
    root.withdraw()  # Esconde a janela principal

    # Selecionar imagem de fundo (ima.jpg)
    imagem_fundo = filedialog.askopenfilename(title="Selecione a imagem de fundo (ima.jpg)", filetypes=[("Imagens", "*.jpg;*.jpeg;*.png")])

    # Selecionar a pasta onde estão as imagens a serem coladas
    pasta_imagens = filedialog.askdirectory(title="Selecione a pasta com as imagens para colar")

    # Selecionar a pasta de saída
    pasta_saida = filedialog.askdirectory(title="Selecione a pasta de saída")

    return imagem_fundo, pasta_imagens, pasta_saida

if __name__ == "__main__":
    # Selecionar as imagens e pasta de saída
    imagem_fundo, pasta_imagens, pasta_saida = selecionar_imagens()

    if imagem_fundo and pasta_imagens and pasta_saida:
        colar_imagem_no_centro(imagem_fundo, pasta_imagens, pasta_saida)
    else:
        print("Seleção cancelada ou inválida.")
