# import logging

# def configurar_logger():
#     logging.basicConfig(filename="execucao.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    

import logging
import os

def configurar_logger():
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(filename="logs/execucao.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    logging.info("Logger configurado com sucesso")
