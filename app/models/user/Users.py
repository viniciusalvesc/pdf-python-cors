"""
Nome do arquivo: Users.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo modelo da tabela users do banco de dados.
"""
from config.alchemy import db

class Users(db.Model):
    __tablename__ = 'users'
    id =  db.Column(db.String, primary_key=True)
    role = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    status = db.Column(db.String)
    createdAt = db.Column(db.Date)
    updatedAt = db.Column(db.Date)
    deletedAt = db.Column(db.Date)

    def serialize(self):
        return {
            'id': self.id,
            'role': self.role,
            'email': self.email,
            'password': self.password,
            'status': self.status,
            'createdAt': self.createdAt.isoformat() if self.createdAt else None,
            'updatedAt': self.updatedAt.isoformat() if self.updatedAt else None,
            'deletedAt': self.deletedAt.isoformat() if self.deletedAt else None,
        }

