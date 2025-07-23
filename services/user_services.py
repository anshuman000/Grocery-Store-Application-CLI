# import getpass
from factories.user_factory import UserFactory
from utils.validate import is_valid_phone, email_validator
from utils.validate import hashed_password
from getpass import getpass

def get_user():
    choice = input("""
1. By Id
2. By email
""")
    if choice == '1':
        id = input("Enter User Id: ")
        user = UserFactory.get_user_by_id(id)
    elif choice == '2':
        email = input("Enter email: ")
        user = UserFactory.get_user_by_email(email)
    else:
        print("❌ Invalid choice.\n")
    print_user(user)

def get_my_detail(user):
    print_user(UserFactory.get_user_by_id(user.id))

def get_all_user():
    users = UserFactory.get_all_user()
    # print(type(users))
    for user in users:
        print_user(user)

def update_user():
    updated_data = credential()
    user = UserFactory.update_user(updated_data["name"], updated_data["email"], updated_data["phone"])
    print("--- Updated Details ---")
    print_user(user)

def update_user_password(user):
    while True:
        new_password = getpass("Enter password: ")
        confirm_password = getpass("Confirm password:")
        if new_password != "" and new_password == confirm_password:
            UserFactory.update_user_password(user.id, hashed_password(new_password))
            print("✅ Password Updated. Login again.")
            exit()
        print("❌  Passwords don't match. Try again.")

def delete_user():
    choice = input("""
1. By Id
2. By email
""")
    if choice == '1':
        id = input("Enter User Id: ")
        UserFactory.delete_user_by_id(id)
        print("--- Deleted Successfuly ---")
    elif choice == '2':
        email = input("Enter email: ")
        UserFactory.delete_user_by_email(email)
        print("--- Deleted Successfuly ---")
    else:
        print("❌ Invalid choice.\n")

def print_user(user):
    for key, value in user.to_dict().items():
        print(f"{key.capitalize():<10}: {value}")

def credential():
    name = input("Enter Name: ").strip()
    while True:
        email = input("Enter email: ").strip()
        result = email_validator(email)
        if result == "Valid Email.":
            print(result)
            break
        print(f"❌ {result} Try again.")
    while True:
        phone = input("Enter Phone: ").strip()
        if is_valid_phone(phone):
            break
        print("❌ Enter valid Phone no.")

    return {"name" : name, "email" : email, "phone" : phone}