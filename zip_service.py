import zipfile
import os

def gerar_zip(lista_arquivos, caminho_zip):
    os.makedirs(os.path.dirname(caminho_zip), exist_ok=True)

    with zipfile.ZipFile(caminho_zip, "w") as zipf:
        for arquivo in lista_arquivos:
            zipf.write(arquivo, os.path.basename(arquivo))

    return caminho_zip
