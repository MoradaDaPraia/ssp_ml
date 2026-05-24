import pandas as pd

caminho_arquivo = "./SPDadosCriminais_2025.xlsx"
nomes_abas = ["JAN_A_JUN_2025", "JUL_A_DEZ_2025"]
listas_dados = []

for nome_aba in nomes_abas:
    # le a aba inteira sem conversoes
    dados = pd.read_excel(caminho_arquivo, sheet_name=nome_aba, na_values=["NULL", ""])
    listas_dados.append(dados)

# junta tudo e salva no csv
dataset_csv = (
    pd.concat(listas_dados, ignore_index=True) if listas_dados else pd.DataFrame()
)

caminho_csv = "./dados_criminais.csv"
dataset_csv = dataset_csv.fillna("")
dataset_csv.to_csv(caminho_csv, index=False)
