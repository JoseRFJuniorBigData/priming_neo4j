import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('db/all_ldt_subs_all_trials3_csv_clean.csv', delimiter=';')


# Adicionar uma coluna "id" autoincrementada
df['id'] = range(1, len(df) + 1)

# Selecionar as colunas desejadas
df = df[['prime', 'target', 'id']]

# Salvar o novo arquivo CSV com as colunas selecionadas e id autoincremento
df.to_csv('db/base_index.csv', index=False, sep=';')

