import os
import sys
import pandas as pd
import logging

from gerar_pdf import gerar_relatorio_pdf
from validar_dados import validando_dados
from logger import configurar_logger
from zip_service import gerar_zip
from email_service import enviar_email

# carregar dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "horas_extras.csv")
df_tabela = pd.read_csv(csv_path)

# gerar relatórios pdfs
lista_pdfs = gerar_relatorio_pdf(df_tabela, pasta_saida="outputs/pdfs")

# validar dados/testar
validando_dados(df_tabela)

# logging
configurar_logger()
logging.info("Inicio da geracao de relatorios")

# gerar zip
zip_path = gerar_zip(lista_pdfs, "outputs/relatorios.zip")
#print(f"ZIP gerado com sucesso em: {zip_path}")

#enviar email
enviar_email(
    destinatario="vasconcellos.vinicius@hotmail.com",
    assunto="Relatórios de Horas Extras",
    corpo="Segue em anexo os relatórios gerados automaticamente.",
    anexo_path=zip_path)