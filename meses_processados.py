import os

def carregar_meses_processados(arquivo="meses_processados.txt"):
    if not os.path.exists(arquivo):
        return set()
    with open(arquivo) as file:
        return set(linha.strip() for linha in file)

def salvar_mes_processado(mes, arquivo="meses_processados.txt"):
    with open(arquivo, "a") as file:
        file.write(mes + "\n")
