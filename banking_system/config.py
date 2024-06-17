import secrets

class Config:
    SECRET_KEY = secrets.token_hex(32)
    MONGO_URI = 'mongodb://localhost:27017/banking_system'
