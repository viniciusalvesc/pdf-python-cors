"""
Nome do arquivo: Users.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo modelo da tabela users do banco de dados.
"""
from config.alchemy import db

class User(db.Model):
    __tablename__ = 'ft_user'
    id =  db.Column(db.String, primary_key=True)
    role = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    status = db.Column(db.String)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    deleted_at = db.Column(db.Date)

    user_info = db.relationship('UserInfo', back_populates='user', uselist=True)
    user_address = db.relationship('UserAddress', back_populates='user', uselist=True)

    def serialize(self):
        return {
            'id': self.id,
            'role': self.role,
            'email': self.email,
            'password': self.password,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'deleted_at': self.deleted_at.isoformat() if self.deleted_at else None,
        }