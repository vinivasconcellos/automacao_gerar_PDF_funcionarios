#test column

import pandas as pd
import pytest
from validar_dados import validando_dados

def test_validar_dados_coluna_faltando():
    df = pd.DataFrame({"Nome": ["Ana"], "Horas Extras": [10]})
    with pytest.raises(ValueError):
        validando_dados(df)

#test zip file

import os
import zipfile
from zip_service import gerar_zip

def test_gerar_zip_cria_arquivo(tmp_path):
    # criar arquivos fake
    arquivo1 = tmp_path / "a.txt"
    arquivo2 = tmp_path / "b.txt"

    arquivo1.write_text("arquivo 1")
    arquivo2.write_text("arquivo 2")

    lista_arquivos = [str(arquivo1), str(arquivo2)]

    caminho_zip = tmp_path / "teste.zip"

    # executar
    zip_resultado = gerar_zip(lista_arquivos, str(caminho_zip))

    # verificar se zip foi criado
    assert os.path.exists(zip_resultado)

    # verificar conteúdo do zip
    with zipfile.ZipFile(zip_resultado, "r") as zipf:
        nomes = zipf.namelist()

    assert "a.txt" in nomes
    assert "b.txt" in nomes
