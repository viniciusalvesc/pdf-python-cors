"""
Nome do arquivo: PaymentHistory.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 16/01/2024
Descrição: Arquivo modelo da tabela ft_payment_history do banco de dados.
"""
from sqlalchemy import ForeignKey, Column, String, Date, DECIMAL, Integer
from sqlalchemy.orm import relationship
from app.db.sqlalchemy import Base

class PaymentHistory(Base):
    __tablename__ = 'ft_payment_history'

    id = Column(String(36), primary_key=True)
    user_id = Column(String, ForeignKey('ft_user.id'), nullable=False, unique=True)
    payment_method_id = Column(String, ForeignKey('ft_payment_method.id'), nullable=False, unique=True)
    payment_address_id = Column(String, ForeignKey('ft_payment_address.id'), nullable=False, unique=True)
    price = Column(DECIMAL(precision=10))
    coupon_id = Column(String)
    discount = Column(DECIMAL(precision=10))
    total_paid = Column(DECIMAL(precision=10))
    installments = Column(Integer)
    created_at = Column(Date)
    updated_at = Column(Date)
    deleted_at = Column(Date)

    user = relationship('User', back_populates='payment_history')
    payment_method = relationship('PaymentMethod', back_populates='payment_history')
    payment_address = relationship('PaymentAddress', back_populates='payment_history')
    