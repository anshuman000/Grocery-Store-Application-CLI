import getpass
from factories.user_factory import UserFactory

def user_menu():
    while True:
        print("""---------USER MENU---------
                    1.Add User
                    2.Get User
                    3.Update User
                    4.Delete User
          """)
        choice = input("Enter here: ")
        match choice:
            case '1':
                get_user()
            case '2':
                update_user()
            case '3':
                delete_user()
            case _:
                print("❌ Invalid choice.\n")
                exit()
    
    
# def get_user():
    
# def update_user():
    
# def delete_user():

def check_user(name, password):
    print("haha")