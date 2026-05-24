## Como instalar as dependências

Crie e ative um ambiente virtual, se ainda não tiver um, e instale os pacotes com:

```bash
pip install -r requirements.txt
```

## Como executar o notebook

Abra o arquivo `main.ipynb` no VS Code ou no Jupyter e execute as células em ordem. O notebook já está pronto para rodar com o arquivo `dados_criminais.csv` presente no repositório.

## Regerar o CSV

Se quiser recriar o arquivo `dados_criminais.csv`, execute o script `converte.py`.

```bash
python converte.py
```

Esse processo pode demorar, porque lê o arquivo Excel completo e consolida as abas antes de salvar o CSV.
