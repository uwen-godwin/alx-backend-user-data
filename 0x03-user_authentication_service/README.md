# User Authentication Service

This project is a user authentication service built using Python, SQLAlchemy, and bcrypt. The service provides essential functionalities like user registration, login, session management, and password reset.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Service](#running-the-service)
  - [Available Endpoints](#available-endpoints)
- [Project Structure](#project-structure)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

This project implements a simple user authentication service with the following functionalities:
- User registration with email and password
- Secure password storage using bcrypt hashing
- User login with session management
- Password reset functionality
- SQLite database for user data storage

## Features

- **User Registration**: Allows new users to create an account by providing an email and password.
- **User Login**: Users can log in to the service with their credentials.
- **Session Management**: Maintains user sessions to allow authenticated access to resources.
- **Password Reset**: Users can reset their password using a reset token.
- **Secure Password Storage**: Passwords are hashed using bcrypt before storage.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.9 or higher
- SQLite (optional, as it's included with Python)
- pip (Python package installer)

## Installation

Follow these steps to install and set up the project:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/uwen-godwin/alx-backend-user-data.git
    cd alx-backend-user-data/0x03-user_authentication_service
    ```

2. **Create and Activate a Virtual Environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the Required Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

    If the `requirements.txt` file is not available, manually install the dependencies:
    ```bash
    pip install sqlalchemy bcrypt
    ```

## Usage

### Running the Service

To run the user authentication service, execute the following command:

```bash
python3 user.py
