"""
Nome do arquivo: Subscription.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 16/01/2024
Descrição: Arquivo modelo da tabela ft_subscription do banco de dados.
"""
from sqlalchemy import ForeignKey, Column, String, Date
from sqlalchemy.orm import relationship
from app.db.sqlalchemy import Base

class Subscription(Base):
    __tablename__ = 'ft_subscription'

    id = Column(String(36), primary_key=True)
    user_id = Column(String, ForeignKey('ft_user.id'), nullable=False, unique=True)
    product_id = Column(String)
    payment_history_id = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
    deleted_at = Column(Date)

    user = relationship('User', back_populates='subscription')
    