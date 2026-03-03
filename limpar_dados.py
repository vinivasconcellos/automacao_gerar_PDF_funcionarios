def extrair_ano_mes(referencia):
    """
    Converte 'Janeiro/2025' → ('2025', '01')
    """

    mapa_meses = {
        "Janeiro": "01",
        "Fevereiro": "02",
        "Março": "03",
        "Abril": "04",
        "Maio": "05",
        "Junho": "06",
        "Julho": "07",
        "Agosto": "08",
        "Setembro": "09",
        "Outubro": "10",
        "Novembro": "11",
        "Dezembro": "12"
    }

    nome_mes, ano = referencia.split("/")
    mes = mapa_meses[nome_mes]

    return ano, mes
