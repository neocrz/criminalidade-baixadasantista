from package.formatar import formatar_prod
from package.check import check_prod
from package import Base, engine, Session, pd
from package.models import *
import os
from datetime import datetime, date

def run_format():
    IN_FILES = "./in-files"
    files = os.listdir(IN_FILES)

    prod_files = []

    for file in files:
        file = IN_FILES + "/" + file

        if check_prod(file):
            prod_files.append(file)

    formatar_prod(prod_files, "test3.csv", "cidades.csv", "ocorrencias.csv")

def commit_ocorrencias():
    session = Session()
    df = pd.read_csv('ocorrencias.csv')

    # Iterar pelas linhas do DataFrame e adicionar as ocorrências à sessão
    for index, row in df.iterrows():
        ocorrencia_name = row['ocorrencia']
        ocorrencia = Ocorrencia(name=ocorrencia_name)
        session.add(ocorrencia)

    # Confirmar as alterações e fechar a sessão
    session.commit()
    session.close()


def commit_cidades():
    session = Session()
    df = pd.read_csv('cidades.csv')

    # Iterar pelas linhas do DataFrame e adicionar as ocorrências à sessão
    for index, row in df.iterrows():
        cidade_name = row['cidade']
        cidade = Cidade(name=cidade_name)
        session.add(cidade)

    # Confirmar as alterações e fechar a sessão
    session.commit()
    session.close()


def data():
    session = Session()
    # Insert data
    ocorrencia1 = Ocorrencia(name='Incidente A')
    cidade1 = Cidade(name='Cidade X')

    # Crie uma instância de Produtividade e estabeleça as relações
    produtividade1 = Produtividade(ocorrencia=ocorrencia1, cidade=cidade1)
    session.add(produtividade1)

    # Commit das mudanças para o banco de dados
    session.commit()

    # Consulta para verificar as relações
    produtividade_query = session.query(Produtividade).first()
    print("Produtividade:", produtividade_query.id)
    print("Ocorrência relacionada:", produtividade_query.ocorrencia.name)
    print("Cidade relacionada:", produtividade_query.cidade.name)

    # Consulta inversa para verificar as relações
    ocorrencia_query = session.query(Ocorrencia).filter_by(id=produtividade_query.ocorrencia_id).first()
    cidade_query = session.query(Cidade).filter_by(id=produtividade_query.cidade_id).first()
    print("Ocorrência associada à Produtividade:", ocorrencia_query.name)
    print("Cidade associada à Produtividade:", cidade_query.name)

    session.close()


def commit_produtividade():
    session = Session()

    # Ler o arquivo CSV usando Pandas
    df = pd.read_csv('produtividade.csv', delimiter=';')

    # Iterar pelas linhas do DataFrame e adicionar as produtividades à sessão
    for index, row in df.iterrows():
        ocorrencia_name = row['ocorrencia']
        
        cidade_name = row['cidade']

        # Pesquisar por nome de ocorrência na tabela Ocorrencia
        ocorrencia = session.query(Ocorrencia).filter_by(name=ocorrencia_name).first()
        
        # Pesquisar por nome de cidade na tabela Cidade
        cidade = session.query(Cidade).filter_by(name=cidade_name).first()
        
        if ocorrencia and cidade:
            produtividade = Produtividade(
                ocorrencia=ocorrencia,
                cidade=cidade,
                qtd=row['valor'],
                
                data=date(int(row['ano']), int(row['mes']), 1)
            )
            session.add(produtividade)

    # Confirmar as alterações e fechar a sessão
    session.commit()
    session.close()

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    run_format()
    commit_ocorrencias()
    commit_cidades()
    commit_produtividade()