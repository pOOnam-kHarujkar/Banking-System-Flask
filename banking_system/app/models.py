from app import mongo
from flask_bcrypt import generate_password_hash
from datetime import datetime

from datetime import datetime

class User:
    @staticmethod
    def create_user(username, password, email):
        hashed_password = generate_password_hash(password).decode('utf-8')
        user_id = mongo.db.users.insert_one({
            'username': username,
            'password': hashed_password,
            'email': email,
            'date_registered': datetime.utcnow()
        }).inserted_id
        return user_id

    @staticmethod
    def find_by_username(username):
        return mongo.db.users.find_one({'username': username})

    @staticmethod
    def get_all_users():
        return list(mongo.db.users.find())

class Transaction:
    @staticmethod
    def create_transaction(user_id, txn_type, amount):
        transaction_id = mongo.db.transactions.insert_one({
            'user_id': user_id,
            'type': txn_type,
            'amount': amount,
            'date': datetime.utcnow()
        }).inserted_id
        return transaction_id

    @staticmethod
    def get_transactions(user_id):
        return list(mongo.db.transactions.find({'user_id': user_id}))

    @staticmethod
    def get_all_transactions():
        return list(mongo.db.transactions.find())
