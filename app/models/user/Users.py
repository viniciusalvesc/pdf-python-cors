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
            'password': self.password,  # Note: You might want to exclude sensitive fields like password
            'status': self.status,
            'createdAt': self.createdAt.isoformat() if self.createdAt else None,
            'updatedAt': self.updatedAt.isoformat() if self.updatedAt else None,
            'deletedAt': self.deletedAt.isoformat() if self.deletedAt else None,
        }

