from factories.connection import get_connection
from models.user import User

class UserFactory:
    @staticmethod
    def create_user(name, email, password, phone):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO USERS (NAME, EMAIL, PASSWORD, PHONE_NO) VALUES (%s, %s, %s, %s)", (name, email, password, phone)
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
    def get_all_user():
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM USERS"
        )
        rows = cursor.fetchall()
        cursor.close()
        db.close()
        return [User.from_row(row) for row in rows]

    @staticmethod
    def update_user(name, email, phone):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE USERS SET NAME = %s, EMAIL = %s, PHONE = %s WHERE USER_ID = %s", (name, email, phone)
        )
        db.commit()
        cursor.close()
        db.close()
        return UserFactory.get_user_by_email(email)
    
    @staticmethod
    def update_user_password(user_id, password):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE USERS SET PASSWORD = %s WHERE USER_ID = %s", (password, user_id,)
        )
        db.commit()
        cursor.close()
        db.close()

    @staticmethod
    def check_email_exists(email: str) -> bool:
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "SELECT EXISTS (SELECT 1 FROM USERS WHERE EMAIL = %s)", (email,)
        )
        exists = cursor.fetchone()[0]
        cursor.close()
        db.close()
        return exists
    
    @staticmethod
    def delete_user_by_id(user_id):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "DELETE FROM USERS WHERE USER_ID = %s", (user_id,)
        )
        db.commit()
        cursor.close()
        db.close()

    @staticmethod
    def delete_user_by_email(email: str):
        db = get_connection()
        cursor = db.cursor()
        cursor.exeute(
            "DELETE FROM USERS WHERE EMAIL = %s", (email,)
        )
        db.commit()
        cursor.close()
        db.close()
