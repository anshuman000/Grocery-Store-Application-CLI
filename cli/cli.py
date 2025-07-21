from utils.auth_service import AuthService
from getpass import getpass
from utils.validate import is_valid_phone, email_validator
# from services.user_services import user_menu

def user_login():
    print(
        """+++++++++ LOG-IN +++++++++
          """)
    email = input("email : ")
    password = getpass("password : ")
    # print(f"{email}  {password}")
    # verify in database
    user = AuthService.login(email, password)
    print(f"✅ Logged in as {user.name} [{user.__class__.__name__}]")
    if user.is_admin:
        # handle_admin_menu()
        print("admin menu")
    else:
        # handle_customer_menu()
        print("customer menu")

            
def user_registration():
    print("""+++++++++ REGISTRATION +++++++++
          """)
    def add_user():
        name = input("Enter name : ")
        while True:
            email = input("Enter email : ").strip() # g@g.com
            result = email_validator(email)
            if result == "Valid Email.":
                print(result)
                break
            print(f"❌ {result} Try again.")
        while True:
            password = getpass.getpass("Enter password : ").strip()
            check_password = getpass.getpass("Confirm password : ").strip()
            if password != "" and password == check_password:
                break
            print("❌  Passwords don't match. Try again.")
        while True:
            phone = input("Enter Phone No.").strip()
            if is_valid_phone(phone):
                break
            print("❌ Enter valid Phone no.")
        user = AuthService.rergistration(name, email, password, phone)
        print("✅ {user.name}, you're registered successfuly.")
        for key, value in user.to_dict().items():       # .item() returns a list of (key, value) pairs form dictionary
            print(f"{key.capitalize():<10}: {value}")
        print(f"{"Is_admin":<10}: YES") if user.is_admin else print(f"{"Is_admin":<10}: NO")