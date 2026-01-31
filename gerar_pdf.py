import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def gerar_relatorio_pdf(df, pasta_saida):
    """
    Gera um PDF por linha do DataFrame com informações de horas extras
    """
    pasta_saida = os.path.join(BASE_DIR, pasta_saida)
    
    os.makedirs(pasta_saida, exist_ok=True)

    for _, linha in df.iterrows():
        nome = linha["Nome"]
        departamento = linha["Departamento"]
        horas_extras = linha["Horas Extras"]
        mes_ref = linha["Referência"]

        documento_pdf = os.path.join(pasta_saida, f"Relatorio_Horas_Extras_{nome}.pdf")

        documento = canvas.Canvas(documento_pdf, pagesize=A4)

        documento.setFont("Helvetica-Bold", 18)
        documento.drawString(100, 750, f"Relatório de Horas Extras")

        documento.setFont("Helvetica", 12)
        distancia = 30
        documento.drawString(100, 700, f"Nome: {nome}")
        documento.drawString(100, 700 - distancia, f"Departamento: {departamento}")
        documento.drawString(100, 700 - 2 * distancia, f"Horas Extras: {horas_extras}")
        documento.drawString(100, 700 - 3 * distancia, f"Mês de Referência: {mes_ref}")
        documento.drawString(100, 700 - 4 * distancia, "Relatório gerado automaticamente via Python")

        documento.save()