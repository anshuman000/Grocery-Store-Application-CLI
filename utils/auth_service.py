import bcrypt
from models.user import User
from models.admin_user import AdminUser
from models.customer_user import CustomerUser
from typing import Optional
from factories.user_factory import UserFactory

class AuthService:

    # checks if the input password is equals to the hashed password
    @staticmethod
    def _check_password(user, plain_password: str) -> bool:
        return  bcrypt.checkpw(plain_password.encode(), user.password.encode())
    
    # converts to bytes -> str
    @staticmethod
    def _hashed_password(password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    #login functon
    def login(email: str, password: str) -> Optional[User]:
        user = UserFactory.get_user_by_email(email)
        if user and AuthService._check_password(user, password):
            if user.is_admin:
                return AdminUser(**user.__dict__)
            return CustomerUser(**user.__dict__)
        else:
            return None
        
    # Registration Function
    def registration(
            name: str,
            email: str,
            password: str,
            phone: str,
    ) -> User:
        password = AuthService._hashed_password(password)
        return UserFactory.create_user(name, email, password, phone)