def validando_dados(df):
    colunas_esperadas = ["Nome", "Departamento", "Horas Extras", "Referência"]

    for col in colunas_esperadas:
        if col not in df.columns:
            raise ValueError(f"Coluna ausente: {col}")

    if df.empty:
        raise ValueError("DataFrame vazio")