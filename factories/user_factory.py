import bcrypt
from factories.connection import get_connection
from models.user import User

class UserFactory:
    @staticmethod
    def create_user(name, email, password, phone):
        db = get_connection()
        cursor = db.cursor()
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        cursor.execute(
            "INSERT INTO USERS (NAME, EMAIL, PASSWORD, PHONE_NO) VALUES (%s, %s, %s, %s)", (name, email, hashed, phone)
        )
        db.commit()
        cursor.close()
        db.close()
        #gives you the AUTO_INCREMENTED id
        return UserFactory.get_user_by_id(cursor.lastrowid)
        
    @staticmethod
    def get_user_by_id(user_id):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM USERS WHERE USER_ID = %s", (user_id,))
        row = cursor.fetchone()
        cursor.close()
        db.close()
        return User.from_row(row) if row else None
    
    @staticmethod
    def get_user_by_email(email: str):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM USERS WHERE EMAIL = %s", (email,)
        )
        row = cursor.fetchone()
        cursor.close()
        db.close()
        return User.from_row(row) if row else None

    @staticmethod
    def update_user(user_id, name, email, password, phone):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE USERS SET NAME = %s, EMAIL = %s, PASSWORD = %s, PHONE = %s WHERE USER_ID = %s", (user_id,)
        )
        db.commit()
        cursor.close()
        db.close()
        return UserFactory.get_user_by_id(user_id)
    
    @staticmethod
    def delete_user(user_id):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "DELETE FROM USERS WHERE USER_ID = %s", (user_id,)
        )
        db.commit()
        cursor.close()
        db.close()