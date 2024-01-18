"""
Nome do arquivo: ProcessedItem.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 16/01/2024
Descrição: Arquivo modelo da tabela ft_processed_item do banco de dados.
"""
from sqlalchemy import ForeignKey, Column, String, Date
from sqlalchemy.orm import relationship
from app.db.sqlalchemy import Base

class ProcessedItem(Base):
    __tablename__ = 'ft_processed_item'

    id = Column(String(36), primary_key=True)
    user_id = Column(String, ForeignKey('ft_user.id'), nullable=False, unique=True)
    external_id = Column(String)
    company_cnpj = Column(String)
    status = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
    deleted_at = Column(Date)

    user = relationship('User', back_populates='processed_item')
    