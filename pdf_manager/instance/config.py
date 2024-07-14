class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pdf_manager.db'
    SECURITY_PASSWORD_SALT = 'your_security_password_salt'
    SECURITY_RECOVERABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_TWO_FACTOR = True
    SECURITY_TWO_FACTOR_SECRET = 'your_two_factor_secret'
    SECURITY_EMAIL_SENDER = 'your_email@example.com'
    MAIL_SERVER = 'smtp.example.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'your_email@example.com'
    MAIL_PASSWORD = 'your_email_password'
