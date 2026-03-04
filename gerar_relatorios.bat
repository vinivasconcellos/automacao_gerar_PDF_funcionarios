@echo off
title Gerador de Relatorios - Horas Extras

echo ===============================
echo Iniciando automacao de relatorios
echo ===============================

REM muda para a pasta onde o .bat está
cd C:\Users\User\Desktop\Documents\Estudos_Programacao\Automacao_Python\Preenchendo-PDF\automacao_gerar_PDF_funcionarios

REM opcional: ativar ambiente virtual
REM call venv\Scripts\activate

REM executar script principal
python main.py

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERRO durante a execucao do script.
    echo Verifique o arquivo de log.
    pause
    exit /b
)

echo.
echo Relatorios gerados e enviados com sucesso!
pause

