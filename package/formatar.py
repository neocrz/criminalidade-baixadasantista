from package import pd
from package.check import detect_encoding




def formatar_prod(files, final, cd_file, oco_file):
  # Criar um novo dataframe vazio para os dados formatados
  df_formatado = pd.DataFrame(columns=['ocorrencia', 'valor', 'mes', 'ano', 'cidade'])
  arquivo_final = final
  df_ocorrencias = pd.DataFrame(columns=['ocorrencia'])
  df_cidades = pd.DataFrame(columns=['cidade'])
  ocorrencias = []
  cidades = []
  
  if isinstance(files, str):
    files = [files]
  for arquivo in files:

    # PEGAR CIDADE
    index_space = arquivo.rfind("Município ")
    index_dot = arquivo.rfind(".")
    cidade = arquivo[index_space + 10:index_dot]
    
    # PEGAR ANO
    with open(arquivo, 'r', encoding='utf-16-le') as file:
      # Lê a primeira linha
      first_line = file.readline().strip()
      
      # Separa os elementos da primeira linha pelo separador do CSV (geralmente vírgula)
      elements = first_line.split(';')
      # Pega o ano no índice 0 e o atribui a uma variável
      ano = elements[0]
    
    # LER O ARQUIVO no PD
    df_original = pd.read_csv(arquivo, encoding='utf-16-le', sep=';', skipinitialspace=True, skiprows=1)
    # removendo a row de totais
    df_original = df_original.drop(df_original.index[-1])
    # Criar listas para as ocorrências e cidades únicas
    

    # Loop através das linhas do dataframe original
    for index, row in df_original.iterrows():
      ocorrencia = row['Ocorrencia']
      cidade = cidade
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
          'cidade': cidade,
          'ano' : ano,
        }
        df_formatado = df_formatado._append(new_row, ignore_index=True)

  for cidade_nome in cidades:
    nova_cidade = {'cidade': cidade_nome}
    df_cidades = pd.concat([df_cidades, pd.DataFrame([nova_cidade])], ignore_index=False)

  for ocorrencia_ in ocorrencias:
    nova_ocorrencia = {'ocorrencia': ocorrencia_}
    df_ocorrencias = pd.concat([df_ocorrencias, pd.DataFrame([nova_ocorrencia])], ignore_index=False)

  # Salvar o dataframe formatado em um novo arquivo CSV
  df_formatado.to_csv(arquivo_final, sep=';', index=False)
  df_ocorrencias.to_csv(oco_file, sep=';', index=False)
  df_cidades.to_csv(cd_file, sep=';', index=False)
  print(arquivo_final, ": salvo")

        