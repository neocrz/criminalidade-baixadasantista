from package import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

class Produtividade(Base):
    __tablename__ = 'produtividades'
    id = Column(Integer, primary_key=True)
    ocorrencia_id = Column(Integer, ForeignKey('ocorrencias.id'))
    cidade_id = Column(Integer, ForeignKey('cidades.id'))
    ocorrencia = relationship('Ocorrencia', back_populates='produtividades')
    cidade = relationship('Cidade', back_populates='produtividades')
    qtd = Column(Integer)
    data = Column(Date)


class Ocorrencia(Base):
    __tablename__ = 'ocorrencias'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    # Relacionamento com Produtividade
    produtividades = relationship('Produtividade', back_populates='ocorrencia')

class Cidade(Base):
    __tablename__ = 'cidades'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    # Relacionamento com Produtividade
    produtividades = relationship('Produtividade', back_populates='cidade')