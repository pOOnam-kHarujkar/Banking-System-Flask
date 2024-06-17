from flask import render_template, redirect, url_for, jsonify, session, request
from app import app
from app.models import User, Transaction
from .forms import RegisterForm, LoginForm, TransactionForm
from app import bcrypt

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        if User.find_by_username(username):
            return jsonify({'message': 'User already exists'}), 400

        user_id = User.create_user(username, password, email)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.find_by_username(username)
        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            return redirect(url_for('dashboard'))

        return jsonify({'message': 'Invalid credentials'}), 401
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user_id=user_id)

@app.route('/balance')
def balance():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    transactions = Transaction.get_transactions(user_id)
    balance = sum([txn['amount'] if txn['type'] == 'deposit' else -txn['amount'] for txn in transactions])
    return render_template('balance.html', balance=balance)

@app.route('/transaction', methods=['GET', 'POST'])
def transaction():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    form = TransactionForm()
    if form.validate_on_submit():
        transaction_type = form.transaction_type.data
        amount = form.amount.data

        if transaction_type not in ['deposit', 'withdraw']:
            return jsonify({'message': 'Invalid transaction type'}), 400

        if transaction_type == 'withdraw':
            transactions = Transaction.get_transactions(user_id)
            balance = sum([txn['amount'] if txn['type'] == 'deposit' else -txn['amount'] for txn in transactions])
            if balance < amount:
                return jsonify({'message': 'Insufficient funds'}), 400

        Transaction.create_transaction(user_id, transaction_type, amount)
        return jsonify({'message': 'Transaction successful'}), 201
    return render_template('transaction.html', form=form)

# Banker Features
@app.route('/accounts')
def accounts():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    users = User.get_all_users()
    return render_template('accounts.html', users=users)

@app.route('/transactions')
def transactions():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    transactions = Transaction.get_all_transactions()
    return render_template('transactions.html', transactions=transactions)
