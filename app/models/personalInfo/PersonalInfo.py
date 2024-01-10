"""
Nome do arquivo: Users.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 09/01/2024
Descrição: Arquivo modelo da tabela personalInfo do banco de dados.
"""
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from config.alchemy import db

class PersonalInfo(db.Model):
    __tablename__ = 'personalInfo'
    
    id = db.Column(db.String, primary_key=True)
    userId = db.Column(db.String, ForeignKey('users.id'), nullable=False, unique=True)
    firstName = db.Column(db.String)
    lastName = db.Column(db.String)
    cpf = db.Column(db.String)
    birthdate = db.Column(db.Date)
    gender = db.Column(db.String)
    phoneNumber = db.Column(db.String)
    userAvatarUrl = db.Column(db.String)
    createdAt = db.Column(db.Date)
    updatedAt = db.Column(db.Date)
    deletedAt = db.Column(db.Date)

    user = db.relationship('Users', back_populates='personal_info')

    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'cpf': self.cpf,
            'birthdate': self.birthdate.isoformat() if self.birthdate else None,
            'gender': self.gender,
            'phoneNumber': self.phoneNumber,
            'userAvatarUrl': self.userAvatarUrl,
            'createdAt': self.createdAt.isoformat() if self.createdAt else None,
            'updatedAt': self.updatedAt.isoformat() if self.updatedAt else None,
            'deletedAt': self.deletedAt.isoformat() if self.deletedAt else None,
        }