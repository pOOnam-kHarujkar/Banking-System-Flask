# Banking-System-Flask
This is a simple banking system implemented using Flask and MongoDB, following the MVC architecture. It allows users to register, login, perform transactions, check balance, and includes optional banker features such as account lists and transaction history.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Contributors](#contributors)

## Features

List of key features of your project.

#### Customer Features:
-  User registration with username, password, and email.
-  User login with access tokens.
#### Perform transactions (deposit, withdraw).
-  Check balance.
-  Optional Banker Features:
-  View account lists.
-  View transaction history.

## Setup

Instructions to set up the project locally.

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/project-name.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure MongoDB URI in config.py:


    ```bash
    MONGO_URI = 'mongodb://localhost:27017/banking_system'
    ```

4. python run.py
 

    ```bash
    python run.py
    ```

5.Access the application in your web browser at http://localhost:5000.

## API Endpoints
- /login: User login endpoint. ]
- /dashboard: User dashboard.
- /balance: Check user balance.
- /transaction: Perform transaction (deposit, withdraw).
- /accounts: Banker feature - View all user accounts.
- /transactions: Banker feature - View all transactions.
## Usage

1. Register a new user by visiting /register.
2. Login with your registered credentials at /login to get an access token.
4. Perform transactions, check balance, and explore banker features.


## Technologies Used

- Flask: Micro web framework for Python.
- MongoDB: NoSQL database for storing user data and transactions.
- Flask-Bcrypt: Hash passwords for secure storage.
- Jinja2: Template engine for rendering HTML templates.

## Project Structure

python-banking-system/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│
│   └── templates/
│       ├── index.html
│       ├── register.html
│       ├── login.html
│       ├── dashboard.html
│       ├── balance.html
│       ├── transaction.html
│       ├── accounts.html
│       └── transactions.html
│
├── config.py
├── requirements.txt
└── run.py

## Contributors

- [Poonam]  (https://github.com/pOOnam-kHarujkar)

