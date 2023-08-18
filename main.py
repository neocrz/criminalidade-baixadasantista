import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('test.csv', sep='|', skipinitialspace=True)

# Criar listas para as ocorrências e cidades únicas
ocorrencias = []
cidades = []

# Loop através das linhas do dataframe
for index, row in df.iterrows():
    ocorrencia = row['ocorrencia']
    cidade = row['cidade']
    valores = row[1:-2]  # Excluindo as colunas 'ocorrencia', 'Total' e 'cidade'
    
    # Adicionar a ocorrência à lista de ocorrências, se ainda não estiver presente
    if ocorrencia not in ocorrencias:
        ocorrencias.append(ocorrencia)
    
    # Adicionar a cidade à lista de cidades, se ainda não estiver presente
    if cidade not in cidades:
        cidades.append(cidade)
    
    # Loop através dos valores e criar as novas linhas formatadas
    for mes, valor in enumerate(valores, start=1):
        new_row = {
            'ocorrencia': ocorrencia,
            'valor': valor,
            'mes': mes,
            'cidade': cidade
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        #df = df._append(new_row, ignore_index=True)

# Reordenar as colunas
df = df[['ocorrencia', 'valor', 'mes', 'cidade']]

# Salvar o dataframe em um novo arquivo CSV
df.to_csv('test_f.csv', index=False)
