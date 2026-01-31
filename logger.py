import logging

def configurar_logger():
    logging.basicConfig(filename="execucao.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    

