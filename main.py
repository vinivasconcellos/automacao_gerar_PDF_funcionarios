import os
import sys
import pandas as pd
import logging

from relatorios_individuais import gerar_relatorio_pdf
from validar_dados import validando_dados
from logger import configurar_logger

# carregar dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "horas_extras.csv")
df_tabela = pd.read_csv(csv_path)

# gerar relatórios
gerar_relatorio_pdf(df_tabela, pasta_saida="outputs/pdfs")

# validar dados/testar
validando_dados(df_tabela)

# logging
configurar_logger()
logging.info("Início da automação")
logging.info("Início da geração de relatórios")
logging.error("Erro ao gerar PDF", exc_info=True)

