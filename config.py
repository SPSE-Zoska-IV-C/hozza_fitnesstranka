class Config:
    SECRET_KEY = "your-secret-key"  # replace with a secure key
    SQLALCHEMY_DATABASE_URI = "sqlite:///fitness.db"  # example DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False