import bcrypt
from factories.user_factory import UserFactory

# phone number validation 
def is_valid_phone(phone: str) -> bool:
    cleanedPhone = phone.replace(" ", "").replace("-","").replace("_","")
    return cleanedPhone.isdigit() and len(cleanedPhone) == 10 and cleanedPhone[0] in ("6789")

# email validation
def email_validator(email: str) -> str:
    if not isinstance(email, str):
        return "Invalid Email."
    
    # if check_email_exists(email):
    #     return "Email already exists."

    if len(email) < 7:
        return "Invalid Email."
    
    # first character must be a lower case alphabet
    if not (email[0].isalpha() and email[0].islower()):
        return "Invalid Email."

    # should be exactly one @
    if email.count("@") != 1:
        return "Invalid Email."
    
    local, domain = email.split("@")
    #domain should have exactly one . and ends with ".com" or ".in"
    if local != "gs" or domain.count(".") != 1 or not email.endswith((".com", ".in")):
        return "Invalid Email."
    
    allowed_characters = ["_", ".", "@"]
    #checks for special characters and spaces
    for char in email:
        if char.isspace():
            return "Invalid Email."
        if not (char.isalnum() or char in allowed_characters):
            return "Invalid Email."

    # return any(
    #     len(email) < 7 or not (email[0].isalpha() and email[0].islower()) or email.count("@") != 1 or
    # )

    return "Valid Email."

# def check_email_exists(email: str) -> bool:
#     return any(user.email == email for user in UserFactory.get_all_user())

def check_email_exists(email: str) -> bool:
    return UserFactory.check_email_exists(email)
        
#password check
def hashed_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()