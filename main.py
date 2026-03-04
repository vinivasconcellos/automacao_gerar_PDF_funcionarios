import os
import sys
import pandas as pd
import logging

from gerar_pdf import gerar_relatorio_pdf
from validar_dados import validando_dados
from logger import configurar_logger
from zip_service import gerar_zip
#from email_service import enviar_email
from meses_processados import carregar_meses_processados, salvar_mes_processado
from limpar_dados import extrair_ano_mes

# carregar dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "horas_extras.csv")
df_tabela = pd.read_csv(csv_path)

# logging
configurar_logger()
logging.info("Start generate the report")

# validar dados/testar
validando_dados(df_tabela)

meses = df_tabela["Referência"].unique()
meses_processados = carregar_meses_processados()

for referencia in meses:
    ano, mes = extrair_ano_mes(referencia)
    chave = f"{ano}-{mes}"

    if chave in meses_processados:
        continue
    
    df_mes = df_tabela[df_tabela["Referência"] == referencia]

    pasta_pdf = f"outputs/pdfs/{ano}/{mes}"
    # gerar relatórios pdfs
    lista_pdfs = gerar_relatorio_pdf(df_mes, pasta_saida=pasta_pdf)
    # gerar zip
    zip_path = gerar_zip(lista_pdfs, f"outputs/zips/{ano}/{mes}.zip")
    
    # enviar_email(
    #             destinatario="empresa@hotmail.com",
    #             assunto=f"Relatórios {referencia}",
    #             corpo="Relatórios automáticos em anexo",
    #             anexo_path=zip_path)
    
    salvar_mes_processado(chave)