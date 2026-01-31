import pandas as pd
import pytest
from validar_dados import validando_dados

def test_validar_dados_coluna_faltando():
    df = pd.DataFrame({"Nome": ["Ana"], "Horas Extras": [10]})
    with pytest.raises(ValueError):
        validando_dados(df)